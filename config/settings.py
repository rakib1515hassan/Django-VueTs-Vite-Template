import os
from pathlib import Path

from config.env import BASE_DIR, env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, '.env'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)
LIVE  = env.bool('LIVE', default=False)


##! Allow Hosts
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS', 
    default=['localhost', '127.0.0.1', '0.0.0.0']
)



##! CORS Headers Allowd
## Allow All Origins (Not Recommended for Production)
CORS_ALLOW_ALL_ORIGINS = env.bool('CORS_ALLOW_ALL_ORIGINS', default=False) ## ⚠️ Only for development! (True)

if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[
        "http://localhost:3000", ## React/Vue development server
        "http://localhost:5173", 
        "http://127.0.0.1:3000",
    ])





##! Application definition

## For Custom Apps Creat (apps/my_apps )
CUSTOM_APPS = [
    'core.apps.CoreConfig',                # core
    'apps.users.apps.UsersConfig',         # users
    'apps.dashboard.apps.DashboardConfig', # dashboard
]

## For Third Party Apps
THIRD_PARTY_APPS = [
    'django_cleanup.apps.CleanupConfig',
]

## Deffault Apps + Django Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'corsheaders',
    
] + CUSTOM_APPS + THIRD_PARTY_APPS





##! Middleware Setup
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',                 ##? CROS Header Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



##! Custom User Model
AUTH_USER_MODEL = 'users.User'
swappable = 'AUTH_USER_MODEL'


##! URL Config
ROOT_URLCONF = 'config.urls'


##! Template Config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                
                ## Apps Template Setup
                # os.path.join(BASE_DIR, 'apps/auth/templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.context_processors.debug', ## Custom
                
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                ##? Custom Context Processor
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


##! Database Setup
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Try to read PostgreSQL config, fallback to None
DB_NAME     = env('DB_NAME', default=None)
DB_USER     = env('DB_USER', default=None)
DB_PASSWORD = env('DB_PASSWORD', default=None)
DB_HOST     = env('DB_HOST', default=None)
DB_PORT     = env('DB_PORT', default=None)

if all([DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
    DATABASES = {
        "default": {
            "ENGINE"   : "django.db.backends.postgresql",
            "NAME"     : DB_NAME,
            "USER"     : DB_USER,
            "PASSWORD" : DB_PASSWORD,
            "HOST"     : DB_HOST,
            "PORT"     : DB_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE' : 'django.db.backends.sqlite3',
            'NAME'   : os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


##! Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True





##! Static and Media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')






# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


##! Some Important Configuration

REMEMBER_ME_EXPIRY = 60 * 60 * 24 * 30   ## 30 days in seconds

OTP_TIMEOUT = 3                          ## OTP timeout set 3 minutes

DEFAULT_PAGINATION_LIMIT = 20            ## Deffault Pagination Limit




##! ================= Package ===================================
from config.packege.drf import *
from config.packege.jwt import *



##! ================= Service ===================================
# from service.email import *
