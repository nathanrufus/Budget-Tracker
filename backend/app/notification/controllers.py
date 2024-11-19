

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from .models import Notification

# Request parser for creating notifications
notification_parser = reqparse.RequestParser()
notification_parser.add_argument('category', type=str, required=True, help="Category is required.")
notification_parser.add_argument('message', type=str, required=True, help="Message is required.")

class NotificationListAPI(Resource):
    @jwt_required()
    def get(self):
        """Retrieve all notifications for the authenticated user."""
        user_id = get_jwt_identity()
        notifications = Notification.query.filter_by(user_id=user_id).all()
        return {"notifications": [notification.serialize() for notification in notifications]}, 200

    @jwt_required()
    def post(self):
        """Create a new notification for the authenticated user."""
        args = notification_parser.parse_args()
        user_id = get_jwt_identity()
        new_notification = Notification(
            user_id=user_id,
            category=args['category'],
            message=args['message']
        )
        db.session.add(new_notification)
        db.session.commit()
        return {"message": "Notification created successfully", "notification": new_notification.serialize()}, 201

class NotificationAPI(Resource):
    @jwt_required()
    def get(self, notification_id):
        """Retrieve a specific notification by ID for the authenticated user."""
        user_id = get_jwt_identity()
        notification = Notification.query.filter_by(id=notification_id, user_id=user_id).first()
        if not notification:
            return {"message": "Notification not found"}, 404
        return {"notification": notification.serialize()}, 200

    @jwt_required()
    def put(self, notification_id):
        """Mark a specific notification as read."""
        user_id = get_jwt_identity()
        notification = Notification.query.filter_by(id=notification_id, user_id=user_id).first()
        if not notification:
            return {"message": "Notification not found"}, 404

        notification.status = "read"
        db.session.commit()
        return {"message": "Notification marked as read", "notification": notification.serialize()}, 200
