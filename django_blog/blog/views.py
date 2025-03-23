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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        
        # Initialize forms with current user data for GET requests
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        context['profile_form'] = ProfileUpdateForm(instance=self.request.user.profile)
        return context

    def post(self, request, *args, **kwargs):
        # Handle POST request with submitted data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():  # Check validity
            user_form.save()  # Save User model data
            profile_form.save()  # Save Profile model data
            return redirect('profile')  # Redirect to refresh page

        # If invalid, re-render template with errors
        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return self.render_to_response(context)