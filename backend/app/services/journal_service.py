from app.models import journal

def get_user_journals(user_id):
    return journal.list_entries(user_id)

def add_journal_entry(user_id, title, body):
    return journal.create_entry(user_id, title, body)

def edit_journal_entry(user_id, entry_id, data):
    return journal.update_entry(user_id, entry_id, data)

def remove_journal_entry(user_id, entry_id):
    return journal.delete_entry(user_id, entry_id)
