FROM python:3.8-slim-buster

# Metadata
LABEL name="JeyDi Cron Test"
LABEL maintainer="JeyDi"
LABEL version="0.1"

ARG YOUR_ENV="virtualenv"

ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.6 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# System deps:
RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y libpq-dev gcc

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /cron
#Copy all the project files
COPY cron ./cron
COPY poetry.lock .
COPY pyproject.toml .
COPY launch.sh .

# Install libraries 
RUN poetry config virtualenvs.create false \
    && poetry install $(test "$YOUR_ENV" = production) --no-dev --no-interaction --no-ansi

# Set the launching script exec
RUN chmod +x cron/launch-schedule.sh

# Launch script
CMD cron/launch-schedule.sh