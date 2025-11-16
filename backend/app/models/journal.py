from flask import current_app
from bson import ObjectId
from app.extensions import mongo
import datetime

def get_db():
    return mongo.db

def list_entries(user_id):
    db = get_db()
    entries = db.journals.find({"user_id": ObjectId(user_id)}).sort("created_at", -1)
    return [
        {
            "id": str(e["_id"]),
            "user_id": str(e["user_id"]),
            "title": e.get("title", ""),
            "body": e.get("body", ""),
            "created_at": e["created_at"].isoformat(),
            "updated_at": e.get("updated_at").isoformat() if e.get("updated_at") else None
        }
        for e in entries
    ]

def create_entry(user_id, title, body):
    now = datetime.datetime.utcnow()
    entry = {
        "user_id": ObjectId(user_id),
        "title": title,
        "body": body,
        "created_at": now,
        "updated_at": now
    }
    db = get_db()
    result = db.journals.insert_one(entry)
    entry["id"] = str(result.inserted_id)
    return entry

def update_entry(user_id, entry_id, data):
    db = get_db()
    db.journals.update_one(
        {"_id": ObjectId(entry_id), "user_id": ObjectId(user_id)},
        {"$set": {
            "title": data.get("title", ""),
            "body": data.get("body", ""),
            "updated_at": datetime.datetime.utcnow()
        }}
    )
    entry = db.journals.find_one({"_id": ObjectId(entry_id)})
    if not entry:
        return None
    entry["id"] = str(entry["_id"])
    return entry

def delete_entry(user_id, entry_id):
    db = get_db()
    result = db.journals.delete_one(
        {"_id": ObjectId(entry_id), "user_id": ObjectId(user_id)}
    )
    return result.deleted_count > 0