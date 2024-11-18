
from flask import Blueprint
from flask_restful import Api
from .controllers import (
    GoalListAPI,
    GoalAPI
)

# Initialize the blueprint
goals_bp = Blueprint('goals', __name__)
api = Api(goals_bp)

# Register the resources with their endpoints
api.add_resource(GoalListAPI, '/goals')
api.add_resource(GoalAPI, '/goals/<int:goal_id>')
