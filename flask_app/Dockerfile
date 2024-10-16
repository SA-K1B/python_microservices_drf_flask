FROM python:3.12
WORKDIR /app
RUN pip install --upgrade pip
# RUN apk add --no-cache gcc musl-dev postgresql-dev
# RUN apt-get update && apt-get install -y postgresql-dev
# RUN apt-get update && apt-get -y install libpq-dev gcc
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV FLASK_APP=app.py
RUN flask db init
CMD [ "sh","entrypoint.sh" ]
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app","--timeout 90"]