from django.urls import path, include

urlpatterns = [
    path('', include('apps.dashboard.urls',  namespace='dashboard')),
]