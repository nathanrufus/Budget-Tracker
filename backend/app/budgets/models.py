from app import db

class Budget(db.Model):
    __tablename__ = "budgets"  # Plural convention for table names
    # __table_args__ = {"extend_existing": True}  # Prevent duplicate table errors

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category": self.category,
            "amount": float(self.amount),
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
        }

    