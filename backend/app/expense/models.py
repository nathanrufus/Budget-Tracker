from app import db

class Expense(db.Model):
    __tablename__ = "expenses"
    # __table_args__ = {"extend_existing": True} 

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date = db.Column(db.Date, nullable=False)

    def serialize(self):
        "dict"
        return {
            "id": self.id,
            "user_id": self.user_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.strftime("%Y-%m-%d"),
        }

    def __repr__(self):
        return f"<Expense {self.id}, {self.category}, {self.amount}>"
