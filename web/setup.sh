#!/bin/bash

if psql -lqt -h postgres -U postgres | cut -d \| -f 1 | grep -w catmaid; then
    echo " ==> Database already exists"
else
    echo " ==> Creating database"
    # Create database and role
    /catmaid/scripts/createuser.sh catmaid catmaid_user p4ssw0rd | sudo  psql -h postgres -U postgres
    # Sync database
    /catmaid/django/projects/mysite/manage.py syncdb
    # Migrate database
    /catmaid/django/projects/mysite/manage.py migrate --all
    # Create static files
    /catmaid/django/projects/mysite/manage.py collectstatic -l --noinput
fi


