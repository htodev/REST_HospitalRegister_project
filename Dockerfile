FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app/src

WORKDIR /app/src

COPY requirements.txt /app/src

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app/src
