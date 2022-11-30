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
    @auth_required
    def get():
        """This view is needed to get user page with available attributes"""
        return user_schema.dump(user_service.get_user_page()), 200

    @staticmethod
    @auth_required
    def patch():
        """This view is needed to update user info, such as name, surname, favorite genre"""
        data = request.json
        return user_service.update_user(data), 204

    @staticmethod
    @auth_required
    def put():
        """This view is needed to update user password"""
        passwords = request.json
        return user_service.update_password(passwords)
