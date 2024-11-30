from flask import Blueprint
from flask_restful import Api
from .controllers import BudgetListAPI, BudgetAPI

# Initialize the blueprint
budgets_bp = Blueprint('budgets', __name__)
api = Api(budgets_bp)

# Register the resources with their endpoints
api.add_resource(BudgetListAPI, '/budgets')
api.add_resource(BudgetAPI, '/budgets/<int:budget_id>')
