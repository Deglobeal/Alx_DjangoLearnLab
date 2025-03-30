from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', obtain_auth_token, name='logout'),
]