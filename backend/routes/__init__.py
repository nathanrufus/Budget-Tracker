from flask import Blueprint
from routes.budgets import budget_blueprint

# Centralized blueprint management
def register_blueprints(app):
    app.register_blueprint(budget_blueprint, url_prefix="/api")
