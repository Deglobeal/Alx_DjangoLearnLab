from django.urls import path
from .views import  list_books_view, home_view, LibraryDetailView 

urlpatterns = [
    path("", home_view, name="home"),
    path("books/", list_books_view, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
]
