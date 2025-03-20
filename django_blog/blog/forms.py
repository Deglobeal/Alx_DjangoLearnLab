from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
