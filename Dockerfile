FROM python:3.13-bullseye

ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    git \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml .

RUN poetry install

COPY . .

RUN chmod 777 entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]


    
