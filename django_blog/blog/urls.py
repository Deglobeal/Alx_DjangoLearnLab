from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    register, profile
)

urlpatterns = [
    # Post-related URLs
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]