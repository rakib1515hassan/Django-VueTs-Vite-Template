


## Django Rest Framework
REST_FRAMEWORK = {

    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
        # Keep SessionAuthentication if you need the browsable API
        'rest_framework.authentication.SessionAuthentication',
    ),

    # 'DEFAULT_FILTER_BACKENDS': [
    #         'django_filters.rest_framework.DjangoFilterBackend'
    #     ],

}