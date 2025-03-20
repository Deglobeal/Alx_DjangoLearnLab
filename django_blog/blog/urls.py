from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    
]