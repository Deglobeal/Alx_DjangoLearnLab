from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
class PostDetailVew(DetailView):
    model = Post
    template_name = 'post_details.html'
    
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'content']