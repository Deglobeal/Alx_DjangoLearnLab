from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'blog/registration.html'
    success_url = reverse_lazy('login')
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'

    # Pass user data to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context