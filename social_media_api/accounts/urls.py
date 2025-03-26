from django.urls import path
from .views import (RegisterView, LoginView, UserProfileView, 
                   FollowUserView, UnfollowUserView,
                   UserFollowingListView, UserFollowersListView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('users/<int:user_id>/following/', UserFollowingListView.as_view(), name='user-following'),
    path('users/<int:user_id>/followers/', UserFollowersListView.as_view(), name='user-followers'),
]