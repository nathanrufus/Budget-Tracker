from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


# import os
from dotenv import load_dotenv

load_dotenv()
jwt=JWTManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # app.config['SQSignupApiLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///budget_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "HJKJIJOKOOJ"  

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)

    from app.auth import auth_bp
    from app.expenses import expenses_bp
    from app.budgets import budgets_bp
    from app.goals import goals_bp
<<<<<<< HEAD
    from app.notification import notifications_bp
    from app.expense import expense_bp
    from app.budgets import budgets_bp 

=======
    from app.reports import reports_bp
    from app.notifications import notifications_bp
    from app.monthly_summaries import monthly_summaries_bp
    
    # Register other blueprints as needed
>>>>>>> cc82d1b9921790cdbf576e7fc604229b2e6c0ca7
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(expenses_bp, url_prefix='/api')
    app.register_blueprint(budgets_bp, url_prefix='/api')
    app.register_blueprint(goals_bp, url_prefix='/api')
    app.register_blueprint(reports_bp, url_prefix='/api')
    app.register_blueprint(notifications_bp, url_prefix='/api')
<<<<<<< HEAD
    app.register_blueprint(expense_bp, url_prefix='/api')
    app.register_blueprint(budgets_bp, url_prefix='/api')
    
=======
    app.register_blueprint(monthly_summaries_bp, url_prefix='/api')


>>>>>>> cc82d1b9921790cdbf576e7fc604229b2e6c0ca7

    return app


