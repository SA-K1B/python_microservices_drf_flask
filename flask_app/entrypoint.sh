#!/bin/bash
flask db init --noinput
flask db migrate --noinput
flask fb upgrade --noinput
gunicorn app:app --bind 0.0.0.0:5000