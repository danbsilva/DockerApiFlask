# -*- coding: utf-8 -*-

from os import getenv
from os.path import dirname, isfile, join
from dotenv import load_dotenv
from src.app import create_app


_ENV_FILE = join(dirname(__file__), '.env')

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


if __name__ == '__main__':
    host = getenv('APP_HOST')
    port = getenv('APP_PORT')
    debug = getenv('DEBUG')

    # executa o servidor web do flask
    create_app().run(
        host=host, port=port, debug=debug,  use_reloader=debug
    )