from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import (PostSerializer, PostCreateSerializer,
                         CommentSerializer, CommentCreateSerializer)
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# User Feed View: Get posts from users the current user follows
class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access
    
    def get_queryset(self):
        # Get posts from users the current user follows
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# Post ViewSet: For handling post CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Only one permission for handling both authentication and author checks
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

# Comment ViewSet: For handling comment CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Only authenticated users can modify comments
    
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id:
            # If a post_id is provided, return comments related to that post
            return Comment.objects.filter(post_id=post_id)
        # If no post_id is provided, return all comments
        return Comment.objects.all()

    def get_serializer_class(self):
        # Use a different serializer for create, update, and partial_update
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

# Like Post View: For liking/unliking posts
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensure authentication is required
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)
