"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import environ
from pathlib import Path


# Environment variables type casting and default value assignment
# If we only want to cast variable type we can do so as seen in ALLOWED_HOSTS
# If we also want to set a default value, we give a tuple with type and a value
# Ex:
#   env = environ.Env(
#       DEBUG=(bool, False),
#       ALLOWED_HOSTS=list,
#   )
# P.S. type casting can be done later on when env is called with cast parameter
# Ex:
#   env(DEBUG, cast=bool, default=False)
# There are also some predefined type casts
# Ex:
#   env.bool("DEBUG", default=False)
#   env.list("ALLOWED_HOSTS")

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import django.db.models

BASE_DIR = Path(__file__).resolve().parent.parent

# Bring environment variables from .env file
environ.Env.read_env(Path.joinpath(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "django_extensions",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'


def gettext_noop(s):
    return s


LANGUAGES = [
    ("en", gettext_noop("English")),
    ("tr", gettext_noop("Turkish")),
]

# Timezone is selected based on deployed server is location
TIME_ZONE = env("TIME_ZONE")

# Internationalization
USE_I18N = True

# Localization
USE_L10N = True

# Timezones
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Media files (user uploaded files; Profile picture, pdf etc.)

MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# UID is better for making project harder to be fiddled by 3rd parties
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
