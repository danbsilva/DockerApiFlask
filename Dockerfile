FROM python:3.9.6

# Definindo a Pasta Raiz
WORKDIR /app

# Copiando aqruivos
COPY requirements.txt .
#COPY .env .
COPY main.py .
COPY setup.py .
COPY ./src ./src

# ENV VARS

ENV DEBUG=True
ENV FLASK_APP="main.py"
ENV FLASK_ENV="development"
ENV APP_HOST="0.0.0.0"
ENV APP_PORT=9999

# KEYS
ENV SECRET_KEY=dee86f03-af0f-4989-aa0b-443167e98efb

# DB
ENV SQLALCHEMY_DATABASE_URI="postgresql://ead:ead@dbead:5432/ead"

# REDIS - CACHE
ENV CACHE_TYPE=redis
ENV CACHE_REDIS_HOST=redisead
ENV CACHE_REDIS_PORT=6379
ENV CACHE_REDIS_DB=API
ENV CACHE_REDIS_URL=redis://redisead:6379/0
ENV CACHE_DEFAULT_TIMEOUT=60000

# venv
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE $APP_PORT

# python setup
RUN python -m venv $VIRTUAL_ENV


# upgrade pip setuptools wheel
RUN pip install --upgrade pip setuptools wheel

# Instalação das Dependencias
RUN pip install -r requirements.txt
RUN pip install psycopg2

CMD flask db init && flask db migrate && flask db upgrade && python main.py

