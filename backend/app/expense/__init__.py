from flask import Blueprint
from flask_restful import Api
from .controllers import ExpenseListAPI,ExpenseAPI


# Initialize the blueprint
expense_bp = Blueprint('expense', __name__)
api = Api(expense_bp)

# Register the resources with their endpoints
api.add_resource(ExpenseListAPI, '/expense')


