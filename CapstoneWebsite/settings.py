"""
Django settings for CapstoneWebsite project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3ibk&ct#(ae5drj0kz@afzfnw#@0qi4z#h$zh1!##_#!l4^j18'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["4d27f317a6d2.ngrok.io", "4acf1b7aa4b6.ngrok.io","127.0.0.1","localhost","django-env.eba-52xwiqzf.us-west-2.elasticbeanstalk.com","fingason.pythonanywhere.com"]

SITE_ID = 1
#STATIC_ROOT = "/home/fingason/CSC-394-Capstone-Website/static"
# or, eg,
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Application definition

INSTALLED_APPS = [
    'CapstoneWebApp.apps.CapstonewebappConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'sslserver',
    'schema_graph',

    'easy_thumbnails',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'bootstrap4',
    'bootstrap_modal_forms',


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

ROOT_URLCONF = 'CapstoneWebsite.urls'

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
                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]

WSGI_APPLICATION = 'CapstoneWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = [
    
    'social_core.backends.open_id.OpenIdAuth',
    
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    
    
    'social_core.backends.fitbit.FitbitOAuth2',

    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',

]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = "dashboard"

LOGOUT_REDIRECT_URL = "dashboard"
#SECURE_SSL_REDIRECT = False


SOCIAL_AUTH_FACEBOOK_KEY = "464890861495806"       # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = "4958b69c763143b1aa5dfe883c1bd947"  # App 
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]

SOCIAL_AUTH_FITBIT_KEY = "22CDBH"       # App ID
SOCIAL_AUTH_FITBIT_SECRET = "6dd214dc3a8a395ca629e5106c23dc92"  # App Secret

WGER_SETTINGS = {
    'USE_RECAPTCHA': False,
    'REMOVE_WHITESPACE': False,
    'ALLOW_REGISTRATION': True,
    'ALLOW_GUEST_USERS': True,
    'EMAIL_FROM': 'wger Workout Manager <wger@example.com>',
    'TWITTER': False
}


