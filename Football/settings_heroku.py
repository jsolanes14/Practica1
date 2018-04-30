from .settings import *
import dj_database_url

# IMPORTANT: to enable these settings in Heroku, set the corresponding environment variable using:
# $> heroku config:set DJANGO_SETTINGS_MODULE=footballRates.settings_heroku


# Parse database configuration from $DATABASE_URL

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

# alguns settings del heroku estan posades a setting.py
