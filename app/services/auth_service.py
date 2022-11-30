from flask import abort
import calendar
import datetime
import jwt

from app.services.user_service import UserService
from constants import JWT_SECRET, JWT_ALGORITHM
from app.services.user_service import secure_service


# ----------------------------------------------------------------
# AuthService class to work with user authentication
class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    @staticmethod
    def convert_user_password_to_hash(data):
        data['password'] = secure_service.make_user_password_hash(data.get('password'))
        return data

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_user_by_email(email)
        if user is None:
            abort(404)
        if not is_refresh:
            if not secure_service.compare_passwords(user.password, password):
                abort(400)
        data = {
            'email': user.email,
            'id': user.id
        }
        # 30 min access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
        # 130 days refresh token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data.get('email')
        return self.generate_tokens(email, None, is_refresh=True)
