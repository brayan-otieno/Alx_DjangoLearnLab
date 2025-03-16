from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic (for example, add additional fields)
        serializer.save()

    # Custom validation can be added here
    def create(self, request, *args, **kwargs):
        data = request.data
        if 'title' not in data:
            return Response({"detail": "Title is required."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Additional custom update logic if necessary
        serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_archived:
            return Response({"detail": "This book cannot be updated."}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
