from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, PostDetailView, PostListView,
    PostCreateView, PostUpdateView, PostDeleteView,
    register, profile
)

urlpatterns = [
    # Post-related URLs
    path('', HomeView.as_view(), name="home"),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]