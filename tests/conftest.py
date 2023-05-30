import pytest
from main import create_app


@pytest.fixture(scope='module')
def app():
    """Instance of main app Flask"""
    return create_app()

