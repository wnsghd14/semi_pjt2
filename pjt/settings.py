import os
from dotenv import load_dotenv
load_dotenv()
"""
Django settings for pjt project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG") == "True"
DEBUG = True
if DEBUG: 
    # MEDIA_URL = "/media/"
    # MEDIA_ROOT = BASE_DIR / "media"
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }
    DEFAULT_FILE_STORAGE = "pjt.storages.MediaStorage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"), # .env 파일에 value 작성
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"), # .env 파일에 value 작성
            "HOST": os.getenv("DATABASE_HOST"), # .env 파일에 value 작성
            "PORT": "5432",
        }
    }    

else:   
    DEFAULT_FILE_STORAGE = "pjt.storages.MediaStorage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"), # .env 파일에 value 작성
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"), # .env 파일에 value 작성
            "HOST": os.getenv("DATABASE_HOST"), # .env 파일에 value 작성
            "PORT": "5432",
        }
    }    


ALLOWED_HOSTS = [
    # "Elastic Beanstalk URL",
    "tripstar-env.eba-rvqec9xz.ap-northeast-2.elasticbeanstalk.com", # 예시입니다. 본인 URL로 해주세요.
    "127.0.0.1",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    "storages",
    'cart',
    "accounts",
    "articles",
    "service_center",
    "django_bootstrap5",
    "django_extensions",
    "imagekit",
    "widget_tweaks",
    "mathfilters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    'django.contrib.humanize',

    # allauth
    'allauth',
    'allauth.account', # 소셜로그인 계정 관리
    'allauth.socialaccount', # 소셜 account 정보 관리

    # provider
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.discord',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # 기본 장고 유저
    'allauth.account.auth_backends.AuthenticationBackend', # 소셜로그인 인증 체계
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/articles/'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pjt.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "context_processors.variable_to_base",
            ],
        },
    },
]

WSGI_APPLICATION = "pjt.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles"
import os

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# MEDIA_ROOT = BASE_DIR / "media"
# MEDIA_URL = "/media/"


# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

# AWS_REGION = "ap-northeast-2"
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
#     AWS_STORAGE_BUCKET_NAME,
#     AWS_REGION,
# )

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# User Model
AUTH_USER_MODEL = "accounts.User"

# Message Framework
# https://docs.djangoproject.com/en/4.1/ref/contrib/messages/
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# # password reset email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = '587'
EMAIL_HOST = 'smtp.naver.com'
EMAIL_HOST_USER = 'sbuni111@naver.com'
EMAIL_HOST_PASSWORD = 'tn!!!qls'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER