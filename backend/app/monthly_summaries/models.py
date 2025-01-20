
from datetime import datetime
from app import db

class MonthlySummary(db.Model):
    __tablename__ = 'monthly_summaries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_expenses = db.Column(db.Numeric(10, 2), nullable=False)
    total_income = db.Column(db.Numeric(10, 2), nullable=True)
    savings_rate = db.Column(db.Numeric(5, 2), nullable=True)
    budget_variance = db.Column(db.Numeric(10, 2), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "month": self.month,
            "year": self.year,
            "total_expenses": float(self.total_expenses),
            "total_income": float(self.total_income) if self.total_income else None,
            "savings_rate": float(self.savings_rate) if self.savings_rate else None,
            "budget_variance": float(self.budget_variance) if self.budget_variance else None
        }
