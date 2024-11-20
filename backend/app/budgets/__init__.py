from flask import Blueprint
from budgets.controllers import budget_blueprint

def register_budget_blueprint(app):
    app.register_blueprint(budget_blueprint, url_prefix="/api/budgets")
