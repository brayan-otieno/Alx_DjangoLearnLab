from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer

class NotificationSerializer(serializers.ModelSerializer):
    actor = UserSerializer()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'read', 'created_at']

    def get_target(self, obj):
        from posts.serializers import PostSerializer
        if obj.target.__class__.__name__ == 'Post':
            return PostSerializer(obj.target, context=self.context).data
        return str(obj.target)