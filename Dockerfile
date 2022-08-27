FROM        python:3.8-bullseye

ENV         PYTHONUNBUFFERED 1

COPY         ./pyproject.toml    /pyproject.toml
COPY         ./poetry.lock       /poetry.lock

#           Install requirements
RUN         pip install pip --upgrade && \
            pip install poetry && \
            poetry config virtualenvs.create false && \
            poetry install --no-interaction

RUN         mkdir /code
WORKDIR     /code

COPY         ./src   .

COPY         ./start.sh          /start.sh
RUN         chmod +x            /start.sh

EXPOSE      8000

ENTRYPOINT  /start.sh