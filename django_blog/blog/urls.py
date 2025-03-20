from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, CustomLogoutView, register


app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', views.profile, name='profile'),
    
]