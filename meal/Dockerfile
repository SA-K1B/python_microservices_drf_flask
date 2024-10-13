FROM python:3.13.0-alpine3.20
WORKDIR /app
RUN pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev postgresql-dev
# RUN apt-get update && apt-get install -y postgresql-dev
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "sh","entrypoint.sh" ]