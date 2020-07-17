"""
Django settings for cohorts_proj project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'rest_framework.authtoken',
    #'rest_auth',
    'django_extensions',

    # Local
    'api.apps.ApiConfig',
    'datasets.apps.DatasetsConfig',
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

ROOT_URLCONF = 'cohorts_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cohorts_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/staticfiles/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

NOTEBOOK_ARGUMENTS = [
    '--ip=0.0.0.0',
    '--port=7777',
    '--no-browser',
]

# TODO
#AUTH_USER_MODEL = 'users.CustomUser'

# TODO
# django-crispy-forms
#CRISPY_TEMPLATE_PACK = 'bootstrap4'

# TODO
# django-allauth config
#LOGIN_REDIRECT_URL = 'home'
#ACCOUNT_LOGOUT_REDIRECT = 'home'

SITE_ID = 1

# TODO
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
#
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST=os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_PORT=os.environ.get('EMAIL_PORT')
# EMAIL_USE_TLS=os.environ.get('EMAIL_USE_TLS')
#
# ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
#
# DEFAULT_FROM_EMAIL = 'admin@harmonization.com'
