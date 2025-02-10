from pathlib import Path
from environs import Env  # Import environs
import os, socket



# Initialize Env and read environment variables
env = Env()
env.read_env()


hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]  # ✅ Allows Debug Toolbar in Docker



# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
SECRET_KEY = env("DJANGO_SECRET_KEY", default="No Secret Key Found")
DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1", "0.0.0.0"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #crispy forms and crispy bootstrap
    'crispy_forms',
    'crispy_bootstrap5',
    #allauth
    'allauth',
    'allauth.account',
    'debug_toolbar',
    #local apps
    'accounts.apps.AccountsConfig', ### This is the path to the accounts app
    'pages.apps.PagesConfig', ### This is the path to the pages app
    'books.apps.BooksConfig', ### This is the path to the books app
]

AUTH_USER_MODEL = 'accounts.CustomUser' # This is the path to the custom user model


MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',  # new 12pm feb 10
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', #enable debug toolbar
    'django.middleware.cache.FetchFromCacheMiddleware',  # new 12pm feb 10
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], ### This is the path to the templates folder
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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL",
        default="postgres://postgres:postgres@db:5432/postgres"
    )
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#New new ############################




STATIC_URL = '/static/' ###Added this line
STATICFILES_DIRS = [BASE_DIR / 'static'] ###Added this line
STATIC_ROOT = BASE_DIR / 'staticfiles' ###Added this line
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage' ###Added this line

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

#allauth settings
LOGIN_REDIRECT_URL = 'home' 

#MORE ALLAUTH SETTINGS

ACCOUNT_LOGOUT_REDIRECT = 'home'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'





##for SSO.  may need to change this to the actual domain i dont underastand this part, will it work on localhost? \

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # new

# MEDIA CONFIGURATION
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")   

#cache settings
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ""

SECURE_SSL_REDIRECT = False
