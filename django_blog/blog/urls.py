from django.urls import path
from .views import HomeView, PostDetailVew

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailVew.as_view(), name="post-detail"),
]