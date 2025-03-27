from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from django.shortcuts import get_object_or_404

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

class NotificationMarkAsReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id, *args, **kwargs):
        notification = get_object_or_404(
            Notification, 
            id=notification_id, 
            recipient=request.user
        )
        notification.mark_as_read()
        return Response({'status': 'marked as read'}, status=status.HTTP_200_OK)

class NotificationMarkAllAsReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        Notification.objects.filter(recipient=request.user, read=False).update(read=True)
        return Response({'status': 'all marked as read'}, status=status.HTTP_200_OK)