from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, View, RedirectView, FormView, UpdateView, CreateView, DeleteView


class Home(TemplateView):
    template_name = 'index.html'

