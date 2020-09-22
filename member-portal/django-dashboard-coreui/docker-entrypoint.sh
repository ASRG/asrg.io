#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Collect database migrations
echo "Collect database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Copy ASRG Sample Data for Events
echo "Copy ASRG Roadmap Data to Container"
docker cp .\ASRG_Roadmap.csv asrg-app:opt/code


# Start guincorn service
echo "Start gunicorn service"
gunicorn --config gunicorn-cfg.py core.wsgi
