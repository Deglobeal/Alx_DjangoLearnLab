from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login!')
            return redirect('login')
        else:
            messages.error(request, 'Error creating your account for you please try cheacking your form for mistakes')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile. Please check the form.')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})
