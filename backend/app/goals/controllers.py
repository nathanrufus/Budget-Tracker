# goals/controllers.py

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from .models import Goal
from datetime import datetime

# Request parsers for input validation
goal_parser = reqparse.RequestParser()
goal_parser.add_argument('target_amount', type=float, required=True, help="Target amount is required and should be a number.")
goal_parser.add_argument('current_savings', type=float, required=False, default=0.0)
goal_parser.add_argument('deadline', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help="Deadline is required in YYYY-MM-DD format.")

update_goal_parser = reqparse.RequestParser()
update_goal_parser.add_argument('target_amount', type=float, required=False)
update_goal_parser.add_argument('current_savings', type=float, required=False)
update_goal_parser.add_argument('deadline', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=False, help="Deadline should be in YYYY-MM-DD format.")

class GoalListAPI(Resource):
    @jwt_required()
    def get(self):
        """Retrieve all goals for the authenticated user."""
        user_id = get_jwt_identity()
        goals = Goal.query.filter_by(user_id=user_id).all()
        return {"goals": [goal.serialize() for goal in goals]}, 200

    @jwt_required()
    def post(self):
        """Create a new goal for the authenticated user."""
        args = goal_parser.parse_args()
        user_id = get_jwt_identity()
        new_goal = Goal(
            user_id=user_id,
            target_amount=args['target_amount'],
            current_savings=args['current_savings'],
            deadline=args['deadline']
        )
        db.session.add(new_goal)
        db.session.commit()
        return {"message": "Goal created successfully", "goal": new_goal.serialize()}, 201

class GoalAPI(Resource):
    @jwt_required()
    def get(self, goal_id):
        """Retrieve a specific goal by ID for the authenticated user."""
        user_id = get_jwt_identity()
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
        if not goal:
            return {"message": "Goal not found"}, 404
        return {"goal": goal.serialize()}, 200

    @jwt_required()
    def put(self, goal_id):
        """Update a specific goal by ID for the authenticated user."""
        args = update_goal_parser.parse_args()
        user_id = get_jwt_identity()
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
        if not goal:
            return {"message": "Goal not found"}, 404

        if args['target_amount'] is not None:
            goal.target_amount = args['target_amount']
        if args['current_savings'] is not None:
            goal.current_savings = args['current_savings']
        if args['deadline'] is not None:
            goal.deadline = args['deadline']

        db.session.commit()
        return {"message": "Goal updated successfully", "goal": goal.serialize()}, 200

    @jwt_required()
    def delete(self, goal_id):
        """Delete a specific goal by ID for the authenticated user."""
        user_id = get_jwt_identity()
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
        if not goal:
            return {"message": "Goal not found"}, 404

        db.session.delete(goal)
        db.session.commit()
        return {"message": "Goal deleted successfully"}, 200
