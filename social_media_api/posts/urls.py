from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, ToggleLikePostView, UserFeedView, PostLikesListView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:post_id>/like/', ToggleLikePostView.as_view(), name='toggle-like-post'),  # handles like/unlike
    path('posts/<int:post_id>/comments/', 
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}), 
         name='post-comments'),
    path('posts/<int:post_id>/comments/<int:pk>/', 
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 
                                 'patch': 'partial_update', 'delete': 'destroy'}), 
         name='comment-detail'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/likes/', PostLikesListView.as_view(), name='post-likes'),
]
