from flask import request
from flask_restx import Resource, Namespace

from helpers import auth_required
from implemented import auth_service, user_service

# ----------------------------------------------------------------
# create namespace
auth_ns = Namespace('auth')


# ----------------------------------------------------------------
# views to handle auth requests
@auth_ns.route('/register')
class AuthViewsRegister(Resource):
    @staticmethod
    def post() -> str:
        """This view is needed to register user in system"""
        try:
            data = request.json
            user = auth_service.convert_user_password_to_hash(data)
            user_service.create_user(user)
            return "", 201
        except Exception:
            return 'user with this email address is already exists'


@auth_ns.route('/login')
class AuthViewsLogin(Resource):
    @staticmethod
    def post() -> str:
        """This view is needed to users log in"""
        data = request.json
        email, password = data.get('email'), data.get('password')
        if None in [email, password]:
            return "", 400
        auth_service.generate_tokens(email, password)
        return "", 201

    @staticmethod
    @auth_required
    def put() -> dict:
        """This view is needed to update tokens"""
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 204
