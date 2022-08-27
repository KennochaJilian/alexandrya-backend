#!/bin/sh

python3 /code/manage.py migrate && python3 /code/manage.py collectstatic --noinput

exec gunicorn  alexandrya.wsgi:application -b 0.0.0.0:8000 --forwarded-allow-ips="*" --workers 3 --worker-class sync --timeout 300