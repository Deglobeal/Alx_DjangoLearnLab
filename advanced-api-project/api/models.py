from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)  
    bio = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)  
    publication_year = models.PositiveIntegerField() 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  
    isbn = models.CharField(max_length=13, unique=True) 

    def __str__(self):
        return self.title
