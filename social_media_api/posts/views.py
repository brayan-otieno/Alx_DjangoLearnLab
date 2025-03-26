from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import (PostSerializer, PostCreateSerializer, 
                         CommentSerializer, CommentCreateSerializer)
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at', 'likes_count']
    ordering = ['-created_at']

    def get_serializer_class(self):
        # Use a different serializer for create, update, and partial_update
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        # Assign the author as the currently logged-in user
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        # Get the post ID from the URL
        post_id = self.kwargs.get('post_id')
        # Filter comments by the specific post ID
        return Comment.objects.filter(post_id=post_id)

    def get_serializer_class(self):
        # Use a different serializer for create, update, and partial_update
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        # Get the post object to associate the comment with
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        # Save the comment with the current user and the post it belongs to
        serializer.save(author=self.request.user, post=post)

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        # Get the post object
        post = self.get_object()
        user = request.user

        # Check if the user has already liked the post
        if post.likes.filter(id=user.id).exists():
            # Remove the like if the user has already liked the post
            post.likes.remove(user)
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            # Add the like if the user hasn't liked the post yet
            post.likes.add(user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)
