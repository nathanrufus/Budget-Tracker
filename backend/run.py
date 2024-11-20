from flask import Flask
from app.models import db
from app.budgets import register_budget_blueprint

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)

register_budget_blueprint(app)

if __name__ == "__main__":
    if app.debug:
        app.run(use_reloader=True)
    else:
        app.run()