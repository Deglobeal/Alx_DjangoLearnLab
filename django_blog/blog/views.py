from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EdithForm
from django.urls import reverse_lazy

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