from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, UserProfileWithFollowsSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser


class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if request.user.follow(user_to_follow):
            return Response({'status': 'following'}, status=status.HTTP_200_OK)
        return Response({'error': 'Unable to follow user'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if request.user.unfollow(user_to_unfollow):
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'Unable to unfollow user'}, status=status.HTTP_400_BAD_REQUEST)

class UserFollowingListView(generics.ListAPIView):
    serializer_class = UserProfileWithFollowsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(CustomUser, id=self.kwargs['user_id'])
        return user.following.all()

class UserFollowersListView(generics.ListAPIView):
    serializer_class = UserProfileWithFollowsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(CustomUser, id=self.kwargs['user_id'])
        return user.followers.all()
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user