from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views import View
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

class Home(TemplateView):
    template_name = 'index.html'

class Register(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


