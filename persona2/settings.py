"""
Django settings for persona2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# openshift is our PAAS for now.
ON_PAAS = 'OPENSHIFT_REPO_DIR' in os.environ

if ON_PAAS:
    SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
else:
    from keys import *
    #SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = not ON_PAAS
DEBUG = DEBUG or 'DEBUG' in os.environ
if ON_PAAS and DEBUG:
    print("*** Warning - Debug mode is on ***")

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!

if ON_PAAS:
    ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS'], socket.gethostname()]
else:
    ALLOWED_HOSTS = []


TEMPLATE_DIRS = [TEMPLATE_PATH,]
CRISPY_TEMPLATE_PACK = 'bootstrap3'
STATICFILES_DIRS = (STATIC_PATH,)

LEAFLET_CONFIG = {
    #'SPACIAL_EXTENT': (5.0, 44.0, 7.5, 46),
    'DEFAULT_CENTER': (50.91, -1.37),
    'DEFAULT_ZOOM': 6,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 18,
    'TILES': "http://pelagios.dme.ait.ac.at/tilesets/imperium/{z}/{x}/{y}.png"
}

TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by allauth template tags
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    # allauth specific context processors
    #"allauth.account.context_processors.account",
    #"allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    #"allauth.account.auth_backends.AuthenticationBackend",
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'personas',
    'crispy_forms',
    #'allauth',
    #'allauth.account',
    'leaflet',
    'djgeojson',
    'sorl.thumbnail',
    'django_markdown',
    'herokuapp',
    #'treasuremap',
    #'allauth.socialaccount',
    # ... include the providers you want to enable:
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'persona2.urls'

WSGI_APPLICATION = 'persona2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if ON_PAAS:
    # determine if we are on MySQL or POSTGRESQL
    if "OPENSHIFT_POSTGRESQL_DB_USERNAME" in os.environ: 
    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',  
                'NAME':     os.environ['OPENSHIFT_APP_NAME'],
                'USER':     os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
                'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
                'HOST':     os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
                'PORT':     os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
            }
        }
        
    elif "OPENSHIFT_MYSQL_DB_USERNAME" in os.environ: 
    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME':     os.environ['OPENSHIFT_APP_NAME'],
                'USER':     os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
                'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
                'HOST':     os.environ['OPENSHIFT_MYSQL_DB_HOST'],
                'PORT':     os.environ['OPENSHIFT_MYSQL_DB_PORT'],
            }
        }
      
else:

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chronicles',
        'USER': 'christopher_allison',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/staticfiles/'

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TEMPLATE_DIRS = [TEMPLATE_PATH,]
STATICFILES_DIRS = (STATIC_PATH,)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LEAFLET_CONFIG = {
    #'SPACIAL_EXTENT': (5.0, 44.0, 7.5, 46),
    'DEFAULT_CENTER': (50.91, -1.37),
    'DEFAULT_ZOOM': 6,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 18,
    'TILES': "http://pelagios.dme.ait.ac.at/tilesets/imperium/{z}/{x}/{y}.png"
}
