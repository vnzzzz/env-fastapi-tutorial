# FROM python:3.9-slim-buster
FROM python:3.9-buster

# package
RUN pip install --upgrade pip && \
    pip install poetry

# poetry
RUN poetry new app
WORKDIR /app
RUN poetry config --local virtualenvs.path ".venv" && \
    poetry config --local virtualenvs.in-project true 
RUN poetry add fastapi uvicorn gunicorn

# app
COPY ./app/ /app/app

RUN apt install curl