from src.extensions.sqlalchemy import db
from src.models.users_model import UserModel


def create(user_data):
    user: UserModel = UserModel(**user_data)
    db.session.add(user)
    db.session.commit()
    return user


def get_by_email(email):
    user = UserModel.query.filter_by(email=email).first()
    return user


def get_one(uuid):
    user = UserModel.query.filter_by(uuid=uuid).first()
    return user


def get_all():
    users = UserModel.query.all()
    return users
