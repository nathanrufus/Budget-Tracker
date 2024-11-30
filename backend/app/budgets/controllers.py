from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from .models import Budget
from datetime import datetime

# Parsers for input validation
budget_parser = reqparse.RequestParser()
budget_parser.add_argument("category", type=str, required=True, help="Category is required.")
budget_parser.add_argument("amount", type=float, required=True, help="Amount is required.")
budget_parser.add_argument("start_date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"), required=True, help="Start date is required in YYYY-MM-DD format.")
budget_parser.add_argument("end_date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"), required=True, help="End date is required in YYYY-MM-DD format.")


update_budget_parser = reqparse.RequestParser()
update_budget_parser.add_argument("category", type=str, required=False)
update_budget_parser.add_argument("amount", type=float, required=False)
update_budget_parser.add_argument("start_date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"), required=False)
update_budget_parser.add_argument("end_date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"), required=False)

class BudgetListAPI(Resource):
    @jwt_required()
    def get(self):
        """Retrieve all budgets."""
        user_id = get_jwt_identity()
        budgets = Budget.query.filter_by(user_id=user_id).all()
        return {"budgets": [budget.serialize() for budget in budgets]}, 200

    @jwt_required()
    def post(self):
        """Create a new budget entry."""
        args = budget_parser.parse_args()  
        user_id = get_jwt_identity()
        new_budget = Budget(
            user_id=user_id,
            category=args["category"],
            amount=args["amount"],
            start_date=args["start_date"],
            end_date=args["end_date"]
        )
        db.session.add(new_budget)
        db.session.commit()
        return {"message": "Budget created successfully", "budget": new_budget.serialize()}, 201


class BudgetAPI(Resource):
    @jwt_required()
    def get(self, budget_id):
        """Retrieve a specific budget by ID."""
        user_id = get_jwt_identity()
        budget = Budget.query.filter_by(id=budget_id, user_id=user_id).first_or_404()
        return {"budget": budget.serialize()}, 200

    @jwt_required()
    def put(self, budget_id):
        """Update an existing budget."""
        args = update_budget_parser.parse_args()
        user_id = get_jwt_identity()
        budget = Budget.query.filter_by(id=budget_id, user_id=user_id).first_or_404()

        if args["category"] is not None:
            budget.category = args["category"]
        if args["amount"] is not None:
            budget.amount = args["amount"]
        if args["start_date"] is not None:
            budget.start_date = args["start_date"]
        if args["end_date"] is not None:
            budget.end_date = args["end_date"]

        db.session.commit()
        return {"message": "Budget updated successfully", "budget": budget.serialize()}, 200

    @jwt_required()
    def delete(self, budget_id):
        """Delete a specific budget."""
        user_id = get_jwt_identity()
        budget = Budget.query.filter_by(id=budget_id, user_id=user_id).first_or_404()
        db.session.delete(budget)
        db.session.commit()
        return {"message": f"Budget {budget_id} deleted successfully"}, 200
