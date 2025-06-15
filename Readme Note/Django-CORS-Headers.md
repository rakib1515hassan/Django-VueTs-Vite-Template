# Setting Up CORS Headers in Django


## 1. Install django-cors-headers

```bash
pip install django-cors-headers
```


## 2. Add to Installed Apps

#### In your settings.py:
```bash
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```


## 3. Add Middleware
#### Place this middleware as high as possible (especially before CommonMiddleware):
```bash
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```



## 4. Configure CORS Settings

#### Add these configurations to your settings.py:

#### For development (allowing all origins - UNSAFE for production)
```bash
CORS_ALLOW_ALL_ORIGINS = True  # Only for development!
```

#### For production (recommended approach)
```bash
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React/Vue development server
    "http://127.0.0.1:3000",
    "https://yourproductiondomain.com",
]

# Optional: Allow credentials (cookies, authorization headers)
CORS_ALLOW_CREDENTIALS = True
```




## 5. Additional Configuration Options
```bash
# Allowed methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Allowed headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Cache duration for preflight requests
CORS_PREFLIGHT_MAX_AGE = 86400  # 1 day
```


## 6. For Nuxt.js/Vue.js specific setup
```bash
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```


## 7. If you need to allow specific headers
```bash
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

## NOTE:-
Important Security Notes
Never use CORS_ALLOW_ALL_ORIGINS = True in production

For production, explicitly list all allowed origins

Combine with proper CSRF protection when using session authentication

If using JWT tokens, make sure to properly configure allowed headers

Testing Your CORS Setup
You can test with curl:

```bash
curl -H "Origin: http://example.com" \
-H "Access-Control-Request-Method: GET" \
-H "Access-Control-Request-Headers: X-Requested-With" \
-X OPTIONS --verbose http://yourdjangoserver.com
```




Additional Middleware Recommendation
Add this for security headers in production:

```bash
MIDDLEWARE = [
    ...
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    ...
]

# Security headers
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True  # If using HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```