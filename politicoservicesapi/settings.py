import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('{0}/.env'.format(BASE_DIR))

SECRET_KEY = os.getenv('SECRET_KEY', 'secret')

DEBUG = True if os.getenv('DEBUG', False) else False

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'storages',
    's3imageservice',
    'oembedservice',
    'tokenservice',
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

ROOT_URLCONF = 'politicoservicesapi.urls'

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

WSGI_APPLICATION = 'politicoservicesapi.wsgi.application'


DATABASES = {}
if 'DATABASE_URL' in os.environ:  # noqa: F821
    DATABASES['default'] = env.db()
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME', None),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', None),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432),
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
WHITENOISE_STATIC_PREFIX = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

###########################
# s3 image service settings
S3IMAGESERVICE_API_AUTHENTICATION_CLASS = (
    'tokenservice.authentication.TokenAuthentication'
)

S3IMAGESERVICE_FILE_MB_LIMIT = 100
S3IMAGESERVICE_S3_UPLOAD_ROOT = 'interactives/uploads/image-service/'
S3IMAGESERVICE_MEDIA_PATH = 'image-service/'
S3IMAGESERVICE_AWS_REGION = 'us-east-2'

S3IMAGESERVICE_AWS_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
S3IMAGESERVICE_AWS_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
S3IMAGESERVICE_AWS_S3_BUCKET = os.getenv('AWS_S3_PUBLISH_BUCKET')
S3IMAGESERVICE_AWS_S3_STATIC_ROOT = os.getenv('AWS_S3_STATIC_ROOT')

#########################
# oembed service settings
OEMBEDSERVICE_API_AUTHENTICATION_CLASS = (
    'tokenservice.authentication.TokenAuthentication'
)
