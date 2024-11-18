# goals/models.py

from datetime import datetime
from app import db

class Goal(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_amount = db.Column(db.Numeric(10, 2), nullable=False)
    current_savings = db.Column(db.Numeric(10, 2), default=0.0)
    deadline = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "target_amount": float(self.target_amount),
            "current_savings": float(self.current_savings),
            "deadline": self.deadline.isoformat(),
            "created_at": self.created_at.isoformat()
        }
