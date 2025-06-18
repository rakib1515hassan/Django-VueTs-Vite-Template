from django.urls import path, include
from apps.dashboard import views

app_name = 'dashboard'


urlpatterns = [
   path('', views.Home.as_view(), name="home"),
    
]
