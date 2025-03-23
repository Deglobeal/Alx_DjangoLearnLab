from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Post
from django.db.models import Q
from .forms import CommentForm, PostForm, EditForm, CustomUserCreationForm, UserUpdateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment
from taggit.models import Tag



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author





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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['post_pk']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

# Update PostDetailView to include comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context
    
class TagView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'
    
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag'))

class SearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
        

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs['tag_slug'])
        return context