# If you don't have settings.py in this directory, you should copy
# this file to settings.py and customize it.

from settings_base import *
import hashlib
import djcelery

DATABASES = {
    'default': {
        'ENGINE': 'custom_postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ATOMIC_REQUESTS': True,              # Wrap every request in a transaction
        'NAME': 'catmaid',      # Or path to database file if using sqlite3.
        'USER': 'catmaid_user',  # Not used with sqlite3.
        'PASSWORD': 'p4ssw0rd',  # Not used with sqlite3.
        'HOST': 'postgres',                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
    }
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
# (You can generate a key with:
# >>> from random import choice
# >>> ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
# '@er^vm3$w#9n$)z3avny*hh+l^#ezv+sx*(72qwp0c%%cg1$i+'
# ... which is how "django-admin startproject" does it.)
SECRET_KEY = 'j1uw0q)4rt5#rh99m%t_^q4i8pnubxv@j4u8*$y3+imvv#j%)s'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/catmaid/django/templates'
)

# Absolute path to the directory that holds user generated data
# like cropped microstacks. Make sure this folder is writable by
# the user running the webserver (and Celery if croppish should
# be used).
# Example: "/var/www/example.org/media/"
MEDIA_ROOT = '/catmaid/media'

# URL that gives access to files stored in MEDIA_ROOT (managed stored
# files). It must end in a slash if set to a non-empty value.
# Example: "http://media.example.org/"
MEDIA_URL = '/files/'

# The URL where static files can be accessed, relative to the domain's root
STATIC_URL = '/static/'
# The absolute local path where the static files get collected to
STATIC_ROOT =  '/catmaid/django/static'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# This is used as a security measure by Django by validating a request's Host
# header. This setting is required when DEBUG is False. A dot in front of the
# host name indicated that also subdomains are allowed.
ALLOWED_HOSTS = ['*']

# Usually, CATMAID's Django back-end is not accessible on a domain's
# root ('/'), but rather a sub-directory like 'catmaid'. Django needs
# to know about this relative path and some web and WSGI servers pass
# this information to Django automatically (e.g. Apache + mod_wsgi).
# However, some don't (e.g. Nginx + Gevent) and the easiest way to
# tell Django were it lives is with the help of the FORCE_SCRIPT_NAME
# variable. It must not have a trailing slash. Therefore, if CATMAID
# runs in the root of a domain, this setting needs to be commented out.
# FORCE_SCRIPT_NAME = '/'

# URL of your CATMAID's Django instance, relative to the domain root
CATMAID_URL = '/'

# Use different cookie names for each CATMAID instance. This increases the size
# of the cookie. So if you run only one instance on this domain, you could also
# remove the next three lines.
COOKIE_SUFFIX = hashlib.md5(CATMAID_URL).hexdigest()
SESSION_COOKIE_NAME = 'sessionid_' + COOKIE_SUFFIX
CSRF_COOKIE_NAME = 'csrftoken_' + COOKIE_SUFFIX

# Local path to store HDF5 files
# File name convention: {projectid}_{stackid}.hdf
HDF5_STORAGE_PATH = '/catmaid/django/hdf5/'

# Importer settings
# If you want to use the importer, please adjust these settings. The
# CATMAID_IMPORT_PATH in (and below) the importer should look for new
# data. The CATMAID_IMPORT_URL refers is the URL as seen from outside
# that gives read access to the CATMAID_IMPORT_PATH.
CATMAID_IMPORT_PATH = '/catmaid/httpdocs/data'
CATMAID_IMPORT_URL = 'http://localhost/data'

## Celery configuration
djcelery.setup_loader()
CELERYD_CONCURRENCY = 1
# Simple django-kumbo message broker
INSTALLED_APPS += ("kombu.transport.django",)
BROKER_URL = 'django://'
