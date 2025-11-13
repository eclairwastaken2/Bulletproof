from app.models.journal import Journal
from bson import ObjectId
import datetime

def list_entries(user_id):
    return Journal.objects(user_id=ObjectId(user_id)).order_by("-created_at")

def create_entry(user_id, title, body):
    entry = Journal(
        user_id = ObjectId(user_id),
        title = title, 
        body = body
    )
    entry.save()
    return entry

def update_entry(user_id, entry_id, data):
    entry = Journal.objects(id=ObjectId(entry_id), user_id=ObjectId(user_id)).first()
    if not entry:
        return None
    
    entry.update(
        title=data.get("title", ""),
        body=data.get("body", ""),
        updated_at=datetime.datetime.utcnow()
    )
    entry.reload()
    return entry

def delete_entry(user_id, entry_id):
    result = Journal.objects(id=ObjectId(entry_id), user_id=ObjectId(user_id)).delete()
    return result > 0