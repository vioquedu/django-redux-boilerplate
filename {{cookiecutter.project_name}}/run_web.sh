#!/bin/sh
# wait for PSQL server to start
sleep 10

cd template_project
# prepare init migration
su -m manager -c "python manage.py makemigrations {{cookiecutter.project_name}}"
# migrate db, so we have the latest db schema
su -m manager -c "python manage.py migrate"
# create super user
su -m manager -c "python manage.py createsuperuser"
# start development server on public ip interface, on port 8000
su -m manager -c "python manage.py runserver 0.0.0.0:8000"
