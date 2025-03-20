from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("Hello world, i am improving on django")
    return render(request, 'base.html')


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})