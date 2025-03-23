from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EdithForm, CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
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
    
    def form_valid(self, form):
        # Automatically handles POST and saves the form
        form.instance.author = self.request.user  # Assign the current user
        return super().form_valid(form) 
    
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
    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})