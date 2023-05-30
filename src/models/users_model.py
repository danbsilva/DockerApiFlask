from src.extensions.sqlalchemy import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    uuid = db.Column(db.String, unique=True, nullable=False, index=True)
    nome = db.Column(db.String,  nullable=False, index=True)
    email = db.Column(db.String, unique=True, nullable=False, index=True)
    password = db.Column(db.String, nullable=False, index=True)
    status = db.Column(db.Boolean)

    def __repr__(self):
        return f'{self.nome}'