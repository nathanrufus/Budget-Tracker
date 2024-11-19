
from flask import Blueprint
from flask_restful import Api
from .controllers import (
    NotificationListAPI,
    NotificationAPI
)

# Initialize the blueprint
notifications_bp = Blueprint('notifications', __name__)
api = Api(notifications_bp)

# Register the resources with their endpoints
api.add_resource(NotificationListAPI, '/notifications')
api.add_resource(NotificationAPI, '/notifications/<int:notification_id>')
