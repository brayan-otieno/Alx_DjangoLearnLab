from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Comment
from notifications.models import Notification

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.author != instance.post.author:
        try:
            Notification.objects.create(
                recipient=instance.post.author,
                actor=instance.author,
                verb="commented on your post",
                target=instance.post
            )
        except Exception as e:
            # Optionally log the error or handle it
            print(f"Error creating notification: {e}")
