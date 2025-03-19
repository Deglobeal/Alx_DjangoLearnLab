from django.contrib import admin
from django.urls import path, include
from blog import views  # 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
]