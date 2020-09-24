#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start guincorn service
echo "Start gunicorn service"
gunicorn --config gunicorn-cfg.py core.wsgi
