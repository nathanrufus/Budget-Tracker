
from flask.views import MethodView
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.expenses.models import Expense
from app.budgets.models import Budget
from .models import MonthlySummary
from datetime import datetime
from app import db

class MonthlySummaryAPI(MethodView):
    @jwt_required()
    def get(self, year, month):
        """Generate a monthly summary of expenses and budgets for the authenticated user."""
        user_id = get_jwt_identity()

        # Calculate total expenses for the month
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
        expenses = Expense.query.filter(Expense.user_id == user_id, Expense.date >= start_date, Expense.date < end_date).all()
        total_expenses = sum(float(expense.amount) for expense in expenses)

        # Calculate total budgets for the month
        budgets = Budget.query.filter(Budget.user_id == user_id, Budget.start_date <= end_date, Budget.end_date >= start_date).all()
        total_budgets = sum(float(budget.amount) for budget in budgets)

        # Calculate savings rate and budget variance
        budget_variance = total_budgets - total_expenses
        savings_rate = (budget_variance / total_budgets * 100) if total_budgets else None

        # Create or update the monthly summary record
        summary = MonthlySummary.query.filter_by(user_id=user_id, month=month, year=year).first()
        if not summary:
            summary = MonthlySummary(user_id=user_id, month=month, year=year)
            db.session.add(summary)

        summary.total_expenses = total_expenses
        summary.total_income = total_budgets  # Assuming income equals budgeted amount
        summary.savings_rate = savings_rate
        summary.budget_variance = budget_variance
        db.session.commit()

        return jsonify(summary.serialize())
