FROM python:3.9.12-slim-buster
ENV PYTHONWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code
RUN apt update && apt install -y libpq-dev gcc
COPY requirements.txt /code
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code
