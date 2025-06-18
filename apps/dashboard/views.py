from django.shortcuts import render
from django.views import View, generic

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'