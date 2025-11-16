from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import journal_service


journal_bp = Blueprint("journal", __name__, url_prefix="/api")

@journal_bp.get("/entries")
@jwt_required()
def list_entries():
    user_id = get_jwt_identity()
    entries = journal_service.list_entries(user_id)
    return jsonify([e.to_dict() for e in entries]), 200

@journal_bp.post("/entries")
@jwt_required()
def create_entry():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    entry = journal_service.create_entry(user_id, data.get("title", ""), data.get("body", ""))
    return jsonify(entry.to_dict()), 201

@journal_bp.put("/entries/<entry_id>")
@jwt_required()
def update_entry(entry_id):
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    entry = journal_service.update_entry(user_id, entry_id, data)
    if not entry:
        return jsonify({"error": "not found"}), 404
    return jsonify(entry.to_dict())

@journal_bp.delete("/entries/<entry_id>")
@jwt_required()
def delete_entry(entry_id):
    user_id = get_jwt_identity()
    ok = journal_service.delete_entry(user_id, entry_id)
    if not ok:
        return jsonify({"error": "not found"}), 404
    return jsonify({"status": "deleted"}), 200