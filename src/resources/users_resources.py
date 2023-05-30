from uuid import uuid4
from flask_restful import Resource, marshal
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from werkzeug.security import generate_password_hash

from src.extensions.cache import cache

from src.schemas.users_schemas import user_response_schema, user_request_schema, \
    UserRequestSchemaDoc, UserResponseSchemaDoc
from src.repositories import users_repository

from src.helpers.token_provider import verify_token
from src.error_types import ERR_USER_ALREADY_EXISTS


class CreateUser(MethodResource, Resource):

    @doc(description='', tags=['Users'])
    @use_kwargs(UserRequestSchemaDoc, location=('json'))
    @marshal_with(UserResponseSchemaDoc)
    def post(self, **kwargs):
        user_data = user_request_schema.parse_args()

        user_db = users_repository.get_by_email(email=user_data['email'])
        if user_db: return {"message": ERR_USER_ALREADY_EXISTS}, 400

        user_data['uuid'] = uuid4().hex
        user_data['password'] = generate_password_hash(password=user_data['password'],
                                                       method='pbkdf2'
                                                       )
        user_data['status'] = True
        new_user = users_repository.create(user_data=user_data)

        return marshal(new_user, user_response_schema), 201


class GetUsers(MethodResource, Resource):

    @doc(description='', tags=['Users'])
    #@verify_token
    def get(self):
        users = users_repository.get_all()
        return marshal(users, user_response_schema, 'users'), 200


class GetUser(MethodResource, Resource):

    @doc(description='', tags=['Users'])
    def get(self, uuid):
        user = users_repository.get_one(uuid=uuid)
        return marshal(user, user_response_schema, 'user'), 200