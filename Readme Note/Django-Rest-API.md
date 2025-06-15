# Installing and Setting Up Django REST Framework (DRF)

## 1. Installation
```bash
pip install djangorestframework
```

#### Markdown support for the browsable API.
```bash
pip install markdown 
```

#### Filtering support
```bash
pip install django-filter
```

#### Simple JWT
```bash
pip install djangorestframework-simplejwt
```


## 2. Add to Installed Apps
#### In your settings.py:
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',            # Add this for DRF
    'django_filters',            # Add this for Django Filter
    'rest_framework_simplejwt',  # Add Simple JWT
    'corsheaders',
    ...
]
```



## 3. Basic REST Framework Settings (Optional but Recommended)
#### In your settings.py:
```bash
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',

        'rest_framework.authentication.TokenAuthentication',          # If using token auth
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # If useing Simple JWT Token

        # Keep SessionAuthentication if you need the browsable API
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```




## 4. Configure JWT Settings
#### Add this to your settings.py to customize JWT behavior:
```bash
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}
```




## 5. Add JWT URLs
#### Include the JWT routes in your project's urls.py:
```bash
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # ... your other URLs ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
```