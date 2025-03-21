from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("Hello world, i am improving on django")
    return render(request, 'base.html')

