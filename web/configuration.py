# Absolute path to the root folder of your CATMAID fork without trailing slash
# e.g. /home/alice/catmaid

abs_catmaid_path = '/catmaid'

# Absolute path to the site-packages folder of your virtual Python environment
# without trailing slash
# e.g. /home/alice/.virtualenvs/catmaid/lib/python2.7/site-packages

abs_virtualenv_python_library_path = '/root/.virtualenvs/catmaid/lib/python2.7/site-packages'

# CATMAID database configuration
catmaid_database_name = 'catmaid'
catmaid_database_username = 'catmaid_user'
catmaid_database_password = 'p4ssw0rd'

# Writable folder to store automatically generated files that are publicly
# visible, e.g. used by by the NeuroHDF export script and the cropping tool.

catmaid_writable_path = '/catmaid/media'

catmaid_hdfs_subdir = 'hdfs'
catmaid_crop_subdir = 'cropping'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# e.g.: Europe/Zurich

catmaid_timezone = 'America/New_York'

# The domain name (server name) which hosts the CATMAID installation
# without http:// and without a trailing slash, e.g.: localhost

catmaid_servername = 'localhost'

# The name of the catmaid subdirectory as seen from the outside
# e.g. for http://localhost/catmaid/ the variable catmaid_subdirectory
# would be 'catmaid'. It should not have a leading or trailing slash.

catmaid_subdirectory = ''
