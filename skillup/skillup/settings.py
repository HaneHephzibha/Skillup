from pathlib import Path
from django.contrib.messages import constants as messages


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = 'django-insecure-e157a6+-e-5ke!i#mmtdzx7a(&d@=!gzubd#7+3r=(9acq!l6n'
DEBUG = True
ALLOWED_HOSTS = []


# Installed apps
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'core.apps.CoreConfig',

]


# Middleware
MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'skillup.urls'


TEMPLATES = [
   {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [BASE_DIR / 'core/templates'],
       'APP_DIRS': True,
       'OPTIONS': {
           'context_processors': [
               'django.template.context_processors.request',
               'django.contrib.auth.context_processors.auth',
               'django.contrib.messages.context_processors.messages',
           ],
       },
   },
]


WSGI_APPLICATION = 'skillup.wsgi.application'


# Database
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',  # change to 'django.db.backends.mysql' if using MySQL
       'NAME': BASE_DIR / 'db.sqlite3',
       # MySQL settings if needed:
       # 'ENGINE': 'django.db.backends.mysql',
       # 'NAME': 'skillup_db',
       # 'USER': 'root',
       # 'PASSWORD': 'root',
       # 'HOST': 'localhost',
       # 'PORT': '3306',
   }
}


# Password validators
AUTH_PASSWORD_VALIDATORS = [
   {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
   {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
   {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
   {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "core/static"]


# Media files (CV uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Login redirect
LOGIN_URL = 'login'

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}