from django.urls import path
from .views import home_view, list_books, LibraryDetailView


urlpatterns = [
    path("", home_view, name="home"),
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
]
