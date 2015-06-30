FROM stackbrew/ubuntu:14.04
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"

RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q \
	imagemagick gcc gfortran apt-file python2.7-dev git \
	libpq-dev libgraphicsmagick++1-dev graphicsmagick \
	libhdf5-serial-dev libboost-dev virtualenvwrapper \
	libboost-python-dev uuid-dev libxml2-dev libxslt1-dev \
	libjpeg-dev libtiff-dev libblas-dev liblapack-dev pkg-config \
	postgresql-client-9.3

# Clone catmaid repository
RUN git clone https://github.com/acardona/CATMAID.git /catmaid

# Add configuration file
ADD configuration.py /catmaid/django/configuration.py

# Add requirements file
ADD requirements.txt /catmaid/requirements.txt
ADD settings.py /catmaid/django/projects/mysite/settings.py
ADD setup.sh /opt/setup.sh

WORKDIR /catmaid
RUN pip install -r /catmaid/requirements.txt
RUN pip install -r /catmaid/django/pip-frozen
RUN mkdir /catmaid/media
RUN chmod 0755 /catmaid/media

WORKDIR /catmaid/django/projects

VOLUME /catmaid/django/static
VOLUME /catmaid/media

CMD ["/bin/bash"]
EXPOSE 8000
