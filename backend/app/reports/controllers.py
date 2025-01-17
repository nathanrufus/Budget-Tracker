# expenses - total expenses, budget - amount, variance
from app.budgets.models import Budget
from app.expense.models import Expense
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
import StringIO
import csv
from flask import make_response

@jwt_required
def func_summary():
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(user_id = user_id).all()
    budgets = Budget.query.filter_by(user_id = user_id).all()
    sum_total_expense = sum(float(exp.amount) for exp in expense if exp is not None) 
    sum_total_budget = sum(float(budg.amount) for budg in budgets if budg is not None) 
    remainder_budget = sum_total_budget - sum_total_expense
    summary = {"total_expense": sum_total_expense, "total_budgets": sum_total_budget , "remainder_budget": remainder_budget}
    return jsonify(summary)

def post(self):
    si = StringIO.StringIO()
    cw = csv.writer(si)
    cw.writerows(csvList)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output