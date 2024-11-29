from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from .models import Expense
from datetime import datetime

expense_blueprint = Blueprint("expenses", __name__)

@expense_blueprint.route("/expenses", methods=["GET"])
@jwt_required()
def get_expenses():
    """Retrieve all expenses for the authenticated user."""
    user_id = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify({"expenses": [expense.serialize() for expense in expenses]}), 200


@expense_blueprint.route("/expenses", methods=["POST"])
@jwt_required()
def create_expense():
    """Add a new expense entry for the authenticated user."""
    data = request.json
    try:
        user_id = get_jwt_identity()
        new_expense = Expense(
            user_id=user_id,
            amount=data["amount"],
            category=data["category"],
            description=data.get("description", ""),
            date=datetime.strptime(data["date"], "%Y-%m-%d"),
        )
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense added successfully", "expense": new_expense.serialize()}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@expense_blueprint.route("/expenses/<int:expense_id>", methods=["PUT"])
@jwt_required()
def update_expense(expense_id):
    """Update a specific expense entry."""
    data = request.json
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

    if not expense:
        return jsonify({"message": "Expense not found"}), 404

    # Update fields
    expense.amount = data.get("amount", expense.amount)
    expense.category = data.get("category", expense.category)
    expense.description = data.get("description", expense.description)
    if "date" in data:
        expense.date = datetime.strptime(data["date"], "%Y-%m-%d")

    db.session.commit()
    return jsonify({"message": "Expense updated successfully", "expense": expense.serialize()}), 200


@expense_blueprint.route("/expenses/<int:expense_id>", methods=["DELETE"])
@jwt_required()
def delete_expense(expense_id):
    """Delete a specific expense entry."""
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

    if not expense:
        return jsonify({"message": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted successfully"}), 200
