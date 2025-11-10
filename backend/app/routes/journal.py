from flask import Blueprint, request, jsonify
from app.extensions import get_db
from app.utils.auth_decorator import jwt_required
from bson import ObjectId
import datetime

journal = Blueprint("journal", __name__)

def _serialize_entry(doc):
    return {
        "id": str(doc["_id"]),
        "user_id": str(doc["user_id"]),
        "title": doc.get("title", ""),
        "body": doc.get("body", ""),
        "created_at": doc.get("created_at").isoformat(),
        "updated_at": doc.get("updated_at").isoformat() if doc.get("updated_at") else None
    }

@journal.route("/entries", methods=["GET"])
@jwt_required
def list_entries():
    db = get_db()
    user_id = request.user_id
    docs = db.entries.find({"user_id": ObjectId(user_id)}).sort("created_at", -1)
    return jsonify([_serialize_entry(d) for d in docs])

@journal.route("/entries", methods=["POST"])
@jwt_required
def create_entry():
    db = get_db()
    body = request.json or {}
    title = body.get("title", "")
    content = body.get("body", "")
    now = datetime.datetime.utcnow()
    res = db.entries.insert_one({
        "user_id": ObjectId(request.user_id),
        "title": title,
        "body": content,
        "created_at": now,
        "updated_at": None
    })
    doc = db.entries.find_one({"_id": res.inserted_id})
    return jsonify(_serialize_entry(doc)), 201

@journal.route("/entries/<entry_id>", methods=["PUT"])
@jwt_required
def update_entry(entry_id):
    db = get_db()
    body = request.json or {}
    update = {"$set": {
        "title": body.get("title", ""),
        "body": body.get("body", ""),
        "updated_at": datetime.datetime.utcnow()
    }}
    result = db.entries.find_one_and_update(
        {"_id": ObjectId(entry_id), "user_id": ObjectId(request.user_id)},
        update,
        return_document=True
    )
    if not result:
        return jsonify({"error": "not found"}), 404
    return jsonify(_serialize_entry(result))

@journal.route("/entries/<entry_id>", methods=["DELETE"])
@jwt_required
def delete_entry(entry_id):
    db = get_db()
    result = db.entries.delete_one({
        "_id": ObjectId(entry_id),
        "user_id": ObjectId(request.user_id)
    })
    if result.deleted_count == 0:
        return jsonify({"error": "not found"}), 404
    return jsonify({"status": "deleted"})