from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Detail view of a single post
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete a post
]
