from django.urls import path
from .views import LibraryDetailView, home_view
from .views import list_books
from .views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from . import views



urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path("", home_view, name="home"),
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
