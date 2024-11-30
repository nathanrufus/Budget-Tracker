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
    from app.goals import goals_bp
    from app.notification import notifications_bp
    from app.expense import expense_bp
    from app.budgets import budgets_bp 

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(goals_bp, url_prefix='/api')
    app.register_blueprint(notifications_bp, url_prefix='/api')
    app.register_blueprint(expense_bp, url_prefix='/api')
    app.register_blueprint(budgets_bp, url_prefix='/api')
    

    return app


