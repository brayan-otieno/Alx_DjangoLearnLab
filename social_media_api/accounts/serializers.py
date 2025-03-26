from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

# Use get_user_model() to handle the custom user model dynamically
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create user using get_user_model().objects.create_user() to ensure proper password hashing and validation
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Generate and return the authentication token
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Authenticate user using the credentials provided
        user = authenticate(**data)
        if user and user.is_active:
            # Generate or get the token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)
            return {'token': token.key}
        raise serializers.ValidationError("Incorrect Credentials")
    
# ... existing serializers ...

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class UserProfileWithFollowsSerializer(serializers.ModelSerializer):
    following = FollowSerializer(many=True, read_only=True)
    followers = FollowSerializer(many=True, read_only=True)
    is_following = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 
                 'following', 'followers', 'is_following', 
                 'followers_count', 'following_count']

    def get_is_following(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user.is_following(obj)
        return False

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()    
