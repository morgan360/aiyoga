from core.settings.base_settings import *
#  Override base settings here
OPEN_API_KEY = os.getenv('OPENAI_API_KEY')
# SECRET_KEY = env('DJANGO_SECRET_KEY')

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DATABASES = {

    'other': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'morganmck$tcsp_project',
        'USER': 'morganmck',
        'PASSWORD': 'Mongo@8899',
        'HOST': 'morganmck.mysql.eu.pythonanywhere-services.com',

    }
}

"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/

import os
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
"""
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-2fgg8%t65_6mcgw4cc6i%kbbl(j-y@lxydyb4rr(4y+nk)x^ov"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ['*']
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     'crispy_forms',
#     "debug_toolbar",
#     "bootstrap5",
#     'django_bootstrap_icons',
#     'ai',
# ]
#
#
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
#
# ROOT_URLCONF = "core.urls"
#
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [os.path.join(BASE_DIR, 'templates')],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = "core.wsgi.application"
#
#
# # Database
# # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/4.1/topics/i18n/
#
# LANGUAGE_CODE = "en-us"
#
# TIME_ZONE = "UTC"
#
# USE_I18N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.1/howto/static-files/
#
# STATIC_URL = "static/"
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
