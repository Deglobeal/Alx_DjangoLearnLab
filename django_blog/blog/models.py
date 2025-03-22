from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='posts'
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']