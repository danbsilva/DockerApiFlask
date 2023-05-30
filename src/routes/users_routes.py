from flask_restful import Api
from src.extensions.csrf import csrf
from src.extensions.swagger import docs
from src.resources.users_resources import CreateUser, GetUsers, GetUser

users = Api(decorators=[csrf.exempt])


def init_app(app):
    users.add_resource(CreateUser, '/users')
    users.add_resource(GetUsers, '/users')
    users.add_resource(GetUser, '/users/<string:uuid>')

    users.init_app(app=app)

    docs.register(CreateUser)
    docs.register(GetUsers)
    docs.register(GetUser)
