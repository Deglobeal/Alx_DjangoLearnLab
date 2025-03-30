from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, UserProfileView, UserListView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', obtain_auth_token, name='logout'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user-list'), 
    
    
    path('users/<int:pk>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]