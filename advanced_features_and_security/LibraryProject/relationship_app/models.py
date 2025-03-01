from django.db import models
from django.conf import settings
from bookshelf.models import Library, Book  # 📌 Fixed: Importing Library and Book Correctly


# 📌 Fixed: Roles Defined Properly
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

# 📌 Fixed: UserProfile References Correct CustomUser Model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# 📌 Fixed: Librarian Model Correctly References Library
class Librarian(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian of {self.library.name}"

# 📌 Fixed: Library_books Model Correctly References Library and Book
class Library_books(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.library.name} - {self.book.title}"
    

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
