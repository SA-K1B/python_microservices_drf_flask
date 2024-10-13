FROM python:3.13-slim
WORKDIR /app
RUN pip install --upgrade pip
RUN apk add postgresql-dev
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt