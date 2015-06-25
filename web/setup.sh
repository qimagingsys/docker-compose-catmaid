#!/bin/bash

# Create database and role
/catmaid/scripts/createuser.sh catmaid catmaid_user p4ssw0rd | sudo  psql -h postgres -U postgres
# Sync database
/catmaid/django/projects/mysite/manage.py syncdb
# Migrate database
/catmaid/django/projects/mysite/manage.py migrate --all
# Create static files
/catmaid/django/projects/mysite/manage.py collectstatic -l --noinput


