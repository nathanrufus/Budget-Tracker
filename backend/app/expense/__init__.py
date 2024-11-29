from expense.controllers import expense_bluerprint
from flask import Blueprint

def register_expense_blueprint(run):
    run.register_blueprint(expense_bluerprint, url_prefix="/api/expenses")
