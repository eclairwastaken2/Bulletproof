from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.auth.cognito import cognito_required
from app.services import journal_service


journal_bp = Blueprint("journal", __name__, url_prefix="/api")

@journal_bp.get("/entries")
@cognito_required
def list_entries():
    user_id = request.user["sub"]
    entries = journal_service.get_user_journals(user_id)
    return jsonify(entries), 200

@journal_bp.post("/entries")
@cognito_required
def create_entry():
    user_id = request.user["sub"]
    data = request.get_json() or {}
    entry = journal_service.add_journal_entry(user_id, data.get("title", ""), data.get("body", ""))
    return jsonify(entry), 201

@journal_bp.put("/entries/<entry_id>")
@cognito_required
def update_entry(entry_id):
    user_id = request.user["sub"]
    data = request.get_json() or {}
    entry = journal_service.edit_journal_entry(user_id, entry_id, data)
    if not entry:
        return jsonify({"error": "not found"}), 404
    return jsonify(entry.to_dict())

@journal_bp.delete("/entries/<entry_id>")
@cognito_required
def delete_entry(entry_id):
    user_id = request.user["sub"]
    ok = journal_service.remove_journal_entry(user_id, entry_id)
    if not ok:
        return jsonify({"error": "not found"}), 404
    return jsonify({"status": "deleted"}), 200