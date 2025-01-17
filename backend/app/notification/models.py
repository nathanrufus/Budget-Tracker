
from datetime import datetime
from app import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="unread")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category": self.category,
            "message": self.message,
            "date_sent": self.date_sent.isoformat(),
            "status": self.status
        }
