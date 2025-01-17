
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.expenses.models import Expense
from app.budgets.models import Budget
from datetime import datetime
import csv
import io

@jwt_required()
def generate_summary():
    """Generate a summary of expenses and budgets for the authenticated user."""
    user_id = get_jwt_identity()
    
    # Fetch user's expenses and budgets
    expenses = Expense.query.filter_by(user_id=user_id).all()
    budgets = Budget.query.filter_by(user_id=user_id).all()

    # Calculate total expenses and total budgets
    total_expenses = sum(float(expense.amount) for expense in expenses)
    total_budgets = sum(float(budget.amount) for budget in budgets)
    remaining_budget = total_budgets - total_expenses

    # Create a summary response
    summary = {
        "total_expenses": total_expenses,
        "total_budgets": total_budgets,
        "remaining_budget": remaining_budget
    }
    return jsonify(summary)

@jwt_required()
def export_csv():
    """Export the user's expenses to a CSV file."""
    user_id = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=user_id).all()

    # Create a CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Amount', 'Category', 'Date', 'Description'])

    for expense in expenses:
        writer.writerow([expense.id, float(expense.amount), expense.category, expense.date, expense.description])

    output.seek(0)

    # Generate a response with the CSV data
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=expenses.csv"
    response.headers["Content-type"] = "text/csv"
    return response
