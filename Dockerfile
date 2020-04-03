# pull base image
FROM python:3.8-alpine

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
COPY Pipfile Pipfile.lock/code
RUN pip install pipenv && pipenv install --system

# set work directory
WORKDIR /code

# copy project
COPY . /code


