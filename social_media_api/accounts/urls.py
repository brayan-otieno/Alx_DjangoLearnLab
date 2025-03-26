from django.urls import path
from .views import (RegisterView, LoginView, UserProfileView, 
                    FollowUserView, UnfollowUserView,
                    UserFollowingListView, UserFollowersListView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),  # Change to match expected
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),  # Change to match expected
    path('users/<int:user_id>/following/', UserFollowingListView.as_view(), name='user-following'),
    path('users/<int:user_id>/followers/', UserFollowersListView.as_view(), name='user-followers'),
]
