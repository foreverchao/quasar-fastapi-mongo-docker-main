FROM python:3.8-slim-buster

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main/ .
COPY src/ .

