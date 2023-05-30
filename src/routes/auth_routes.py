from flask_restful import Api
from src.extensions.csrf import csrf
from src.extensions.swagger import docs
from src.resources.auth_resources import LoginUser, LogoutUser

auth = Api(decorators=[csrf.exempt])


def init_app(app):

    auth.add_resource(LoginUser, '/auth/login')
    auth.add_resource(LogoutUser, '/auth/logout')

    auth.init_app(app=app)

    docs.register(LoginUser)
    docs.register(LogoutUser)

