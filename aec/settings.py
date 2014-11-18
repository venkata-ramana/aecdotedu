"""
Django settings for aec project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v0akky6(rez6iad8_y6$h-59d3-*p%%$1ij*%w+a#s(=xo0i)^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
                  'news_events',
                  'gallery',
                  'placements',
                  'about',
                  'toppers',
                  'downloads',
                  'academics',
                  'infrastructure',
                  'journals'
                  )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aec.urls'

WSGI_APPLICATION = 'aec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True
STATICFILES_DIRS = (
                    # Put strings here, like "/home/html/static" or "C:/www/django/static".
                    # Always use forward slashes, even on Windows.
                    # Don't forget to use absolute paths, not relative paths.
                    os.path.join(
                                 os.path.dirname(__file__),
                                 'static',
                                 ),
                    )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
                 # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
                 # Always use forward slashes, even on Windows.
                 # Don't forget to use absolute paths, not relative paths.
                 os.path.join(BASE_DIR, 'templates'),)

ABSOLUTE_PATH = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

MEDIA_ROOT ='media'
MEDIA_URL = '/'
