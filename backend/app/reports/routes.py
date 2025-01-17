
from flask.views import MethodView
from .controllers import generate_summary, export_csv

class ReportSummaryAPI(MethodView):
    """API endpoint for generating summary reports."""
    def get(self):
        return generate_summary()

class CSVExportAPI(MethodView):
    """API endpoint for exporting expenses to CSV."""
    def get(self):
        return export_csv()
