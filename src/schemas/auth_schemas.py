from flask_restful import reqparse
from flask_restful import fields
from email_validator import validate_email
from src.extensions.marshmallow import ma
from marshmallow import fields as ma_fields


def email(email_str):
    """Return email_str if valid, raise an exception in other case."""
    if validate_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))


# POST
auth_request_schema = reqparse.RequestParser(bundle_errors=True)
auth_request_schema.add_argument('email',  type=email, required=True, location='json')
auth_request_schema.add_argument('password',  type=str,  required=True, location='json')

# GET
auth_reposnse_schema = {
    'uuid': fields.String,
    'nome': fields.String,
    'status': fields.Boolean
}


class AuthRequestSchemaDoc(ma.Schema):
    email = ma_fields.String(required=True)
    password = ma_fields.String(required=True)


class AuthResponseSchemaDoc(ma.Schema):
    token = ma_fields.Str()
    message = ma_fields.Str()
