# docker-compose-catmaid

## Prerequisites
Docker Engine [Mac](https://docs.docker.com/installation/mac/) [Ubuntu](https://docs.docker.com/installation/ubuntulinux/) or [Windows](https://docs.docker.com/installation/windows)
[Docker Compose](https://docs.docker.com/compose/install/)

## Usage
Clone the repository
```
git clone git@github.com:qimagingsys/docker-compose-catmaid.git
```

Now, when you run `docker-compose up -d`, Compose will pull a CATMAID image, build an image for Nginx, and start everything up:
````
docker-compose up -d
```

Get the container ID for the CATMAID web application container using `docker ps`
```bash
$ docker ps
CONTAINER ID        IMAGE                        COMMAND                CREATED             STATUS              PORTS                    NAMES
a35f6c94a05b        qimagingsys_nginx:latest     "/usr/sbin/nginx"      5 hours ago         Up 5 hours          0.0.0.0:80->80/tcp       qimagingsys_nginx_1
3bc855644bb0        qimagingsys/catmaid:latest   "/usr/local/bin/guni   5 hours ago         Up 5 hours          0.0.0.0:8000->8000/tcp   qimagingsys_web_1
60a5053eafe0        qimagingsys/postgres:9.3     "/docker-entrypoint.   5 hours ago         Up 5 hours          0.0.0.0:5432->5432/tcp   qimagingsys_postgres_1
ed73bc2d7737        qimagingsys/postgres:9.3     "/docker-entrypoint.   5 hours ago         Up 5 hours          5432/tcp                 qimagingsys_data_1
```

Run the `/opt/setup.sh` script for the database

```
docker exec -i -t 3bc855644bb0 /opt/setup.sh
```
Note: You will replace `3bc855644bb0` with your own container ID

Create a superuser account for CATMAID. Executing the command `/catmaid/django/projects/mysite/manage.py createsuperuser` will prompt for a username, email and password

```
docker exec -i -t 3bc855644bb0 /catmaid/django/projects/mysite/manage.py createsuperuser
```

