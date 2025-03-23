from django.urls import path
# Corrected import line in urls.py
from .views import HomeView, PostDetailView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]