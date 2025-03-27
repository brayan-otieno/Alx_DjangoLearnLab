from django.urls import path
from .views import (NotificationListView, 
                   NotificationMarkAsReadView,
                   NotificationMarkAllAsReadView)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:notification_id>/read/', NotificationMarkAsReadView.as_view(), name='notification-read'),
    path('read-all/', NotificationMarkAllAsReadView.as_view(), name='notification-read-all'),
]