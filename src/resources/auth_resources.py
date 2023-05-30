from flask_restful import Resource, marshal, request
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from werkzeug.security import check_password_hash

from src.extensions.cache import cache

from src.schemas.auth_schemas import auth_request_schema, auth_reposnse_schema, \
    AuthResponseSchemaDoc, AuthRequestSchemaDoc
from src.repositories import users_repository

from src.helpers.token_provider import create_token_jwt

from src.settings import TIMEOUT_CHACHE_BLACKLIST_TOKEN_JWT
from src.error_types import ERR_USER_OR_PASS_INVALID


class LoginUser(MethodResource, Resource):

    @doc(description='', tags=['Auth'])
    @use_kwargs(AuthRequestSchemaDoc, location=('json'))
    @marshal_with(AuthResponseSchemaDoc)
    def post(self, **kwargs):
        user_data = auth_request_schema.parse_args()

        # Validar se o usuário existe e se a senha confere
        user_db = users_repository.get_by_email(email=user_data['email'])
        if not user_db or not check_password_hash(user_db.password, user_data['password']):
            return {"message": ERR_USER_OR_PASS_INVALID}, 401

        token = create_token_jwt(marshal(user_db, auth_reposnse_schema))

        cache.set(user_db.uuid,
                  token,
                  timeout=TIMEOUT_CHACHE_BLACKLIST_TOKEN_JWT)

        return {"token": token}, 200


class LogoutUser(MethodResource, Resource):

    @doc(description='', tags=['Auth'])
    def post(self):
        cache.set(f'TOKEN_BLACKLIST_{request.headers["Authorization"]}',
                  f'{request.headers["Authorization"]}',
                  timeout=TIMEOUT_CHACHE_BLACKLIST_TOKEN_JWT)

        return '', 200