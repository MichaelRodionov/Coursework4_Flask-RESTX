from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.models import UserSchema
from helpers import auth_required
from implemented import user_service


# ----------------------------------------------------------------
# create namespace and schema to serialize/deserialize
user_ns = Namespace('user')
user_schema = UserSchema()


# ----------------------------------------------------------------
# views to handle user requests
@user_ns.route('/')
class UserView(Resource):
    @staticmethod
    @user_ns.doc(description='Get user page', responses={200: 'OK', 401: 'Unauthorized'})
    @auth_required
    def get() -> dict:
        """This view is needed to get user page with available attributes"""
        user = user_service.get_user_page()
        return user_schema.dump(user), 200

    @staticmethod
    @user_ns.doc(description='Update user info', responses={204: 'No Content', 401: 'Unauthorized'})
    @auth_required
    def patch() -> None:
        """This view is needed to update user info, such as name, surname, favorite genre"""
        data = request.json
        user_service.update_user(data)
        return "", 204

    @staticmethod
    @user_ns.doc(description='Update user password', responses={204: 'No Content', 401: 'Unauthorized'})
    @auth_required
    def put() -> None:
        """This view is needed to update user password"""
        passwords = request.json
        user_service.update_password(passwords)
        return "", 204
