from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from .models import CustomUser
from .forms import RegisterForm

class RegistrationView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form':form})
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'users/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm(request)
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context)
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'Username or password error!')
            return render(request, 'users/login.html', {'form':form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')













