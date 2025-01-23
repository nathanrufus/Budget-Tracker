
from flask import Blueprint
from .routes import ReportSummaryAPI, CSVExportAPI

# Initialize the blueprint
reports_bp = Blueprint('reports', __name__)

# Register the routes
reports_bp.add_url_rule('/reports/summary', view_func=ReportSummaryAPI.as_view('report_summary'))
reports_bp.add_url_rule('/reports/export_csv', view_func=CSVExportAPI.as_view('export_csv'))
