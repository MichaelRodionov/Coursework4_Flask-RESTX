from flask import request
from flask_restx import Resource, Namespace

from configuration.auth_util import auth_required
from configuration.implemented import auth_service, user_service

# ----------------------------------------------------------------
# create namespace
auth_ns = Namespace('auth')


# ----------------------------------------------------------------
# views to handle auth requests
@auth_ns.route('/register/')
class AuthViewsRegister(Resource):
    @staticmethod
    @auth_ns.doc(description='Register new user', responses={201: 'Created'})
    def post() -> str:
        """
        This view is needed to register user in system
        """
        try:
            data = request.json
            user = auth_service.convert_user_password_to_hash(data)
            user_service.create_user(user)
            return "", 201
        except Exception:
            return 'user with this email address is already exists'


@auth_ns.route('/login/')
class AuthViewsLogin(Resource):
    @staticmethod
    @auth_ns.doc(description='Log in user', responses={201: 'No Content', 400: 'Bad Request', 401: 'Unauthorized'})
    def post() -> str or dict:
        """
        This view is needed to users log in
        :return: Authorization tokens (access token and refresh token)
        """
        data = request.json
        email, password = data.get('email'), data.get('password')
        if None in [email, password]:
            return "", 400
        return auth_service.generate_tokens(email, password), 201

    @staticmethod
    @auth_ns.doc(description='Update tokens', responses={204: 'No Content', 400: 'Bad Request', 401: 'Unauthorized',
                                                         404: 'Not Found'})
    @auth_required
    def put() -> dict:
        """
        This view is needed to update tokens
        :return: Updated authorization tokens (access token and refresh token)
        """
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 204
