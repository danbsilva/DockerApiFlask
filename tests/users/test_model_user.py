from src.models.users_model import UserModel

user = {
    'id': '',
    'uuid': '',
    'nome': '',
    'email': '',
    'password': '',
}

model = UserModel(**user)


def test_uuid_field_exists():
    """
    Verifico se o campo uuid existe
    """
    assert 'uuid' in model.__dict__


def test_nome_field_exists():
    """
    Verifico se o campo uuid existe
    """
    assert 'nome' in model.__dict__


def test_email_field_exists():
    """
    Verifico se o campo uuid existe
    """
    assert 'email' in model.__dict__


def test_password_field_exists():
    """
    Verifico se o campo uuid existe
    """
    assert 'password' in model.__dict__