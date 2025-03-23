from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('post_update', args=(str(self.id)))
        
        
    def save(self, *args, **kwargs):
        # Custom logic (e.g., generate a slug)
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    