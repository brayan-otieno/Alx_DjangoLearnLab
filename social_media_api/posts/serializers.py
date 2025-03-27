from rest_framework import serializers
from .models import Post, Comment, Like
from accounts.serializers import UserSerializer

# LikeSerializer to handle likes
class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['user', 'created_at']

# CommentSerializer with likes functionality
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)  # Include likes for the comment
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'likes', 'likes_count', 'is_liked']
        read_only_fields = ['author', 'created_at', 'updated_at', 'likes']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

# PostSerializer to handle posts and likes
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)  # Include likes for the post
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 
                  'updated_at', 'comments', 'likes', 'likes_count', 'is_liked']
        read_only_fields = ['author', 'created_at', 'updated_at', 'comments', 'likes']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

# PostCreateSerializer to create a post
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

# CommentCreateSerializer to create a comment
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
