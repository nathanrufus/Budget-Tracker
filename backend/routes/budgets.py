from flask import Blueprint, jsonify, request
from app.models import db, Budget
from utils.serializers import serialize_budget
from datetime import datetime
#Crud

budget_blueprint = Blueprint("budgets", __name__)

@budget_blueprint.route('/budgets', methods=['POST'])
def create_budget():
    """Create a new budget entry."""
    data = request.json
    try:
        new_budget = Budget(
            user_id=data["user_id"],
            category=data["category"],
            amount=data["amount"],
            start_date=datetime.strptime(data["start_date"], "%Y-%m-%d"),
            end_date=datetime.strptime(data["end_date"], "%Y-%m-%d"),
        )
        db.session.add(new_budget)
        db.session.commit()
        return jsonify({"message": "Budget created successfully", "budget": serialize_budget(new_budget)}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@budget_blueprint.route('/budgets', methods=['GET'])
def get_budgets():
    """Get all budgets."""
    budgets = Budget.query.all()
    return jsonify([serialize_budget(budget) for budget in budgets]), 200

@budget_blueprint.route('/budgets/<int:budget_id>', methods=['GET'])
def get_budget(budget_id):
    """Get a budget by ID."""
    budget = Budget.query.get_or_404(budget_id)
    return jsonify(serialize_budget(budget)), 200

@budget_blueprint.route('/budgets/<int:budget_id>', methods=['PUT'])
def update_budget(budget_id):
    """Update an existing budget."""
    budget = Budget.query.get_or_404(budget_id)
    data = request.json
    try:
        budget.category = data.get("category", budget.category)
        budget.amount = data.get("amount", budget.amount)
        budget.start_date = datetime.strptime(data.get("start_date", str(budget.start_date)), "%Y-%m-%d")
        budget.end_date = datetime.strptime(data.get("end_date", str(budget.end_date)), "%Y-%m-%d")
        db.session.commit()
        return jsonify({"message": "Budget updated successfully", "budget": serialize_budget(budget)}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 400

@budget_blueprint.route('/budgets/<int:budget_id>', methods=['DELETE'])
def delete_budget(budget_id):
    """Delete a budget."""
    budget = Budget.query.get_or_404(budget_id)
    db.session.delete(budget)
    db.session.commit()
    return jsonify({"message": f"Budget {budget_id} deleted successfully"}), 200
