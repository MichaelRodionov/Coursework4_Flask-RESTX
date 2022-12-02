import base64
import hashlib
import hmac
import jwt
from flask import abort, request

from constants import HASH_ALGORITHM, PWD_ENCODE, PWD_SALT, PWD_ITERATIONS, JWT_SECRET, JWT_ALGORITHM


# ----------------------------------------------------------------
# SecureService class to make password protected by hash, compare passwords and decode token to get user_id
class SecureService:
    @staticmethod
    def make_user_password_hash(password: str) -> bytes:
        """Method to encode str password"""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            HASH_ALGORITHM,
            password.encode(PWD_ENCODE),
            PWD_SALT,
            PWD_ITERATIONS
        ))

    @staticmethod
    def compare_passwords(password_hash: bytes, other_password: str) -> bool:
        """Method to compare hash password and str password"""
        return hmac.compare_digest(base64.b64decode(password_hash), hashlib.pbkdf2_hmac(
            HASH_ALGORITHM,
            other_password.encode(PWD_ENCODE),
            PWD_SALT,
            PWD_ITERATIONS
        ))

    @staticmethod
    def get_email_or_id_from_token(is_id=False, is_email=False) -> str:
        """Method to get user id from token"""
        if 'Authorization' not in request.headers:
            abort(401)
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            user_data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if not is_email:
                uid = user_data.get('id')
                return uid
            if not is_id:
                uemail = user_data.get('email')
                return uemail
        except Exception as e:
            print('JWT Decode Error: ', e)
            abort(401)
