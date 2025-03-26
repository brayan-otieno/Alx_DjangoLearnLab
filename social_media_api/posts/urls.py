from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikePostView, UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', 
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}), 
         name='post-comments'),
    path('posts/<int:post_id>/comments/<int:pk>/', 
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 
                               'patch': 'partial_update', 'delete': 'destroy'}), 
         name='comment-detail'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]