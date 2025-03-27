from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser
from django.utils import timezone

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)
    
    # Generic foreign key to any related object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['-timestamp']  

    def __str__(self):
        return f"{self.actor.username} {self.verb}"

    def mark_as_read(self):
        self.read = True
        self.save()
