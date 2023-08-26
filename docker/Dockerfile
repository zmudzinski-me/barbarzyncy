FROM python:3.9-buster as base

ENV PYTHONUNBUFFERED=1 \
    PYSETUP_PATH=/opt/pysetup \
    # this is paths where our requirements and venv will be created
    VENV_PATH=/opt/pysetup/.venv \
    POETRY_HOME=/opt/poetry \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libxml2 \
        libpq5 \
        curl \
        default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

FROM base as build

ENV POETRY_VERSION=1.6.1
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY ./pyproject.toml ./poetry.lock ./

ARG DEBUG=false
RUN poetry install -E prod $(test ! $DEBUG && echo "--no-dev")

FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PROJECT_DIR=/project/app \
    VENV_PATH=/opt/pysetup/.venv

ENV PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/src \
    MYPYPATH=$PYTHONPATH:$PROJECT_DIR/src \
    PATH="$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libxml2 \
        libpq5 \
        curl \
        default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

ARG GROUP_GID=101
ARG USER_UID=1000

RUN addgroup --system --gid $GROUP_GID django \
    && useradd -m -g django -u $USER_UID django \
    && mkdir -p /project/media /project/static

COPY --from=build $VENV_PATH $VENV_PATH

WORKDIR $PROJECT_DIR
COPY . $PROJECT_DIR

RUN chown -R django: /project
RUN chmod +x /project/app/docker/entrypoint.sh

USER django

# Can't use PROJECT_DIR env var in exec ENTRYPOINT
ENTRYPOINT ["/project/app/docker/entrypoint.sh"]
CMD ["uwsgi"]
EXPOSE 8000
