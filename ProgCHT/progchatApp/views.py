from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views import View

class Home(TemplateView):
    template_name = 'index.html'
