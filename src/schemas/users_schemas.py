from flask_restful import reqparse
from flask_restful import fields
from src.extensions.marshmallow import ma
from marshmallow import fields as ma_fields

# POST
user_request_schema = reqparse.RequestParser(bundle_errors=True)
user_request_schema.add_argument('nome',  type=str, required=True, location='json')
user_request_schema.add_argument('email',  type=str,  required=True, location='json')
user_request_schema.add_argument('password', type=str, required=True, location='json',)

# GET
user_response_schema = {
    'uuid': fields.String,
    'nome': fields.String,
    'email': fields.String,
    'status': fields.Boolean
}


class UserRequestSchemaDoc(ma.Schema):
    nome = ma_fields.String(required=True)
    email = ma_fields.Email(required=True)
    password = ma_fields.String(required=True)


class UserResponseSchemaDoc(ma.Schema):
    message = ma_fields.String(default='Success')
    uuid = ma_fields.String(required=True)
    nome = ma_fields.String(required=True)
    email = ma_fields.Email(required=True)
    status = ma_fields.Boolean(required=True)