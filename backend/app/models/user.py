from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    name = db.StringField(max_length=20)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow())

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "email": self.email, 
            "name": self.name, 
            "created_at": self.created_at,
        }