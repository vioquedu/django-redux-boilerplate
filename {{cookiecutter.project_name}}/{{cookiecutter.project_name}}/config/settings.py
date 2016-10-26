
# -*- coding: utf-8 -*-
"""
Django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ
import os
import datetime
from jinja2 import Environment, FileSystemLoader
# Load enviroment
root = environ.Path(__file__) - 2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env     = environ.Env()


# Read configuration file
environ.Env.read_env('config/env_file.py')


# DEBUG
DEBUG          = env.bool('DEBUG')
# END DEBUG

# SECRET KEY DEFINITION
SECRET_KEY = env('SECRET_KEY')

# Define site root
SITE_ROOT = root()

# Site id
SITE_ID    = 1
SITE_NAME = '{{cookiecutter.project_name}}'
    
# Application definition
ROOT_URLCONF     = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# Allowed hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

APPEND_SLASH = True

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_jwt',
    # Useful template tags:
    'django.contrib.humanize',
    'docs',
    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'braces',        
    'django_extensions',
    'webpack_loader',
)
    
# Apps specific for this project go here.
LOCAL_APPS = (
    'apps',
    'apps.common',
    # Your stuff: custom apps go here
)
    
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

# DOCS ROOT
DOCS_ROOT = 'docs/_build/html/'
DOCS_ACCESS = 'staff'

# IPYTHON SETTINGS
IPYTHON_ARGUMENTS = [
    '--ext', 'django_extensions.management.notebook_extension',
]

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION

# MIGRATIONS CONFIGURATION
#MIGRATION_MODULES = {
#    'sites': 'contrib.sites.migrations'
#}
# END MIGRATIONS CONFIGURATION


# FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
# END FIXTURE CONFIGURATION
    
# EMAIL CONFIGURATION
#EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
# END EMAIL CONFIGURATION

# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""{{cookiecutter.author_email}}""", '{{cookiecutter.author_email}}'),
)
    
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION
    
# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {'default': env.db() } 
# END DATABASE CONFIGURATION
    
# GENERAL CONFIGURATION
    
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = '{{cookiecutter.project_timezone}}'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = '{{cookiecutter.language}}'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# END GENERAL CONFIGURATION
# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
            # Your stuff: custom template context processors go here
            'apps.common.context_processors.site_info',
            ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            ]
        }
    }
]

# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# URL Configuration
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'
# End URL Configuration

# AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
# END AUTHENTICATION CONFIGURATION

@classmethod
def post_setup(cls):
    cls.DATABASES['default']['ATOMIC_REQUESTS'] = True

# Your common stuff: Below this line define 3rd party library settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
    
JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(60),
    'JWT_PAYLOAD_HANDLER': 'apps.accounts.views.jwt_payload_handler',
}
    
# EMAIL CONFIGURATION
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS       = True
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_PWD')
EMAIL_PORT          = 587
EMAIL_ADMIN         = env.list('EMAIL_ADMIN')
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
# END EMAIL CONFIGURATION

# JINJA CONFIG
JINJA_TEMPLATES = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(BASE_DIR, 'path/to/templates/dir')),
    trim_blocks=False)

### WEBPACK LOADER
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundle/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/src/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

if not DEBUG:
    WEBPACK_LOADER.update({
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/src/webpack-stats-prod.json'),
    })


