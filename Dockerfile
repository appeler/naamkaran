FROM python:3.11-slim

RUN mkdir /usr/src/naamkaran

WORKDIR /naamkaran

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .
