from flask_restful import Resource,reqparse
from flask_jwt_extended import create_access_token
from .models import User
from app import db

signup_parser=reqparse.RequestParser()
signup_parser.add_argument("email",type=str ,required=True, help="Email is required")
signup_parser.add_argument("password",type=str ,required=True, help="Password is required")

login_parser=reqparse.RequestParser()
login_parser.add_argument("email",type=str ,required=True, help="Email is required")
login_parser.add_argument("password",type=str ,required=True, help="Password is required")

class SignupApi(Resource):
    def post(self):
        args=signup_parser.parse_args()
        email ,password=args['email'],args['password']

        if User.query.filter_by(email=email).first():
            return {"message":"User already exists"} ,400
        new_user=User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return {"message":"user created successfully" ,"user":new_user.serialize()},201
class LoginApi(Resource):
    
    def post(self):
        args=login_parser.parse_args()
        email ,password=args['email'],args['password']

        user =User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return{
                "message":"login successfully",
                "user":user.serialize(),
                "token":access_token
            },200
        return {"message":"Invalid credentials"},401



