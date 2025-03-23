from django.urls import path
from .views import HomeView, PostDetailVew, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailVew.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]