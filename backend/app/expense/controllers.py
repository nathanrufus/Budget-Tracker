from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from .models import Expense
from datetime import datetime

# Parsers for input validation
expense_parser = reqparse.RequestParser()
expense_parser.add_argument("amount", type=float, required=True, help="Amount is required.")
expense_parser.add_argument("category", type=str, required=True, help="Category is required.")
expense_parser.add_argument("description", type=str, required=False, default="")
expense_parser.add_argument("date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"), required=True, help="Date is required in YYYY-MM-DD format.")

update_expense_parser = reqparse.RequestParser()
update_expense_parser.add_argument("amount", type=float, required=False)
update_expense_parser.add_argument("category", type=str, required=False)
update_expense_parser.add_argument("description", type=str, required=False)
update_expense_parser.add_argument("date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"), required=False)

class ExpenseListAPI(Resource):
    @jwt_required()
    def get(self):
        """Retrieve all expenses for the authenticated user."""
        user_id = get_jwt_identity()
        expenses = Expense.query.filter_by(user_id=user_id).all()
        return {"expenses": [expense.serialize() for expense in expenses]}, 200

    @jwt_required()
    def post(self):
        """Add a new expense entry."""
        args = expense_parser.parse_args()
        user_id = get_jwt_identity()
        new_expense = Expense(
            user_id=user_id,
            amount=args["amount"],
            category=args["category"],
            description=args["description"],
            date=args["date"],
        )
        db.session.add(new_expense)
        db.session.commit()
        return {"message": "Expense added successfully", "expense": new_expense.serialize()}, 201


class ExpenseAPI(Resource):
    @jwt_required()
    def put(self, expense_id):
        """Update a specific expense."""
        args = update_expense_parser.parse_args()
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

        if not expense:
            return {"message": "Expense not found"}, 404

        if args["amount"] is not None:
            expense.amount = args["amount"]
        if args["category"] is not None:
            expense.category = args["category"]
        if args["description"] is not None:
            expense.description = args["description"]
        if args["date"] is not None:
            expense.date = args["date"]

        db.session.commit()
        return {"message": "Expense updated successfully", "expense": expense.serialize()}, 200

    @jwt_required()
    def delete(self, expense_id):
        """Delete a specific expense."""
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

        if not expense:
            return {"message": "Expense not found"}, 404

        db.session.delete(expense)
        db.session.commit()
        return {"message": f"Expense {expense_id} deleted successfully"}, 200
