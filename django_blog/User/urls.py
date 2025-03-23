from django.urls import path
from .views import UserRegisterView
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_http_methods


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path(
        'User/logout/',
        require_http_methods(['GET', 'POST'])(LogoutView.as_view()),
        name='logout'),
]