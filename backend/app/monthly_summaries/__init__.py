
from flask import Blueprint
from .controllers import MonthlySummaryAPI

# Initialize the blueprint
monthly_summaries_bp = Blueprint('monthly_summaries', __name__)

# Register the route for the monthly summary API
monthly_summaries_bp.add_url_rule('/monthly_summaries/<int:year>/<int:month>', view_func=MonthlySummaryAPI.as_view('monthly_summary'))
