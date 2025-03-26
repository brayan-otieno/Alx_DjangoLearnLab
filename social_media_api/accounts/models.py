from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)
    
    # Following relationships
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following_set',  # Changed the related_name to a unique value
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        """Follow another user"""
        if user != self and not self.following.filter(id=user.id).exists():
            self.following.add(user)
            return True
        return False

    def unfollow(self, user):
        """Unfollow a user"""
        if user != self and self.following.filter(id=user.id).exists():
            self.following.remove(user)
            return True
        return False

    def is_following(self, user):
        """Check if following a specific user"""
        return self.following.filter(id=user.id).exists()
