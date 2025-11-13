from app.extensions import db
import datetime

class Journal(db.Document):
    user_id = db.ObjectIdField(required=True)
    title = db.StringField(default="")
    body = db.StringField(default="")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow())
    updated_at = db.DateTimeField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }