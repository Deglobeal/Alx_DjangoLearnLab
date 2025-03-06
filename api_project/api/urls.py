from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList viewfrom django.contrib import admin
]
