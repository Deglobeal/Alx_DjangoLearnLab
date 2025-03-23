from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EdithForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin 

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-published_date']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = EdithForm
    template_name = 'blog/update.html'
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')
    
class RegisterView(CreateView):
    form_class = UserCreationForm  # Or your custom registration form
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login') 
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'

    # Pass user data to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context