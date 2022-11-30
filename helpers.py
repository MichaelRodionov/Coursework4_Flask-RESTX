import jwt
from flask import request, abort

from constants import JWT_SECRET, JWT_ALGORITHM


# ----------------------------------------------------------------
# 'auth_required' decorator to make requests denied, when user is not authorized
def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode Error: ', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper
