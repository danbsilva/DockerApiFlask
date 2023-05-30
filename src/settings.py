from datetime import datetime, timedelta
from os import getenv, path

BASE_DIR = path.dirname(path.realpath(__file__))

# APP
DEBUG = eval(getenv('DEBUG').title())
FLASK_ENV = getenv('FLASK_ENV')
APP_PORT = int(getenv('APP_PORT'))
APP_HOST = getenv('APP_HOST')

# KEYS
ALGORITHM = 'HS512'
SECRET_KEY = getenv('SECRET_KEY')

# DB
SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
BUNDLE_ERRORS = True

# TOKEN JWT
EXPIRE_TOKEN_JWT = datetime.utcnow() + timedelta(minutes=int(60))
TIMEOUT_CHACHE_BLACKLIST_TOKEN_JWT = 60 * 60

# REDIS
CACHE_TYPE = getenv('CACHE_TYPE')
CACHE_REDIS_HOST = getenv('CACHE_REDIS_HOST')
CACHE_REDIS_PORT = getenv('CACHE_REDIS_PORT')
CACHE_REDIS_DB = getenv('CACHE_REDIS_DB')
CACHE_REDIS_URL = getenv('CACHE_REDIS_URL')
CACHE_DEFAULT_TIMEOUT = getenv('CACHE_DEFAULT_TIMEOUT')

# EXTENSIONS
EXTENSIONS = [
     'src.extensions.sqlalchemy:init_app',
     'src.extensions.csrf:init_app',
     'src.extensions.cache:init_app',
     'src.extensions.marshmallow:init_app',
     'src.extensions.swagger:init_app',
     'src.routes.users_routes:init_app',
     'src.routes.auth_routes:init_app',
#
 ]




