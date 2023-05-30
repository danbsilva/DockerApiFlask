from datetime import datetime, timedelta
from functools import wraps
from os import getenv
from typing import Any, Union

from flask import request
from jose import jwt

from src.extensions.cache import cache
from src.settings import EXPIRE_TOKEN_JWT, ALGORITHM


def create_token_jwt(user: Union[str, Any]) -> str:
    payload = {
        "exp": EXPIRE_TOKEN_JWT,
        "user": user,
        
    }
    to_encode = payload
    encoded_jwt = jwt.encode(to_encode, getenv('SECRET_KEY'), algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(func):

    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        try:
            token = request.headers['Authorization']
        except:
            ...

        if not token: return {'message': 'Token not found'}, 401

        cache_exists = cache.get(f'TOKEN_BLACKLIST_{token}')
        if cache_exists: return {"message": "Token is invalid"}, 401

        try:
            jwt.decode(token.replace('Bearer ', ''), getenv('SECRET_KEY'), algorithms=[ALGORITHM])

        except Exception as e:
            return {'message': 'Token is invalid'}, 401

        return func(*args, **kwargs)

    return decorated

