from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


# from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # return HttpResponse("Hello world, i am improving on django")
    return render(request, 'base.html')

