from flask import Blueprint
from flask_restful import Api
from .controllers import SignupApi ,LoginApi

auth_bp=Blueprint("auth",__name__)
api=Api(auth_bp)

api.add_resource(SignupApi, "/signup")
api.add_resource(LoginApi, "/login")