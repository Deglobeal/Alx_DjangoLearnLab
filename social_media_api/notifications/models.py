from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Notification(models.Model):  # Fixed typo in class name
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='notifications',
        on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct', 'target_id')
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']