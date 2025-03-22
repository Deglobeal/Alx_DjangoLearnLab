from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "Users/register.html", {"form": form})
