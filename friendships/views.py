from rest_framework import generics
from .models import SnapFriendship
from .serializers import SnapFriendshipSerializer
from snap_it.permissions import IsOwnerOrReadOnly


class SnapFriendshipList(generics.ListCreateAPIView):
    """
    Handles listing and creation of SnapFriendships.
    """
    serializer_class = SnapFriendshipSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return SnapFriendship.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnapFriendshipDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Used for retrieving, updating, and deleting individual SnapFriendships.
    Users can only access their own SnapFriendships.
    """
    serializer_class = SnapFriendshipSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = SnapFriendship.objects.all()
