from rest_framework import generics
from .models import SnapFriendship
from .serializers import SnapFriendshipSerializer
from snap_it.permissions import IsOwnerOrReadOnly

"""
The code defines two API views using Django REST Framework's
generic views to manage SnapFriendship objects. The SnapFriendshipList
view allows listing all SnapFriendship instances and creating new ones,
ensuring the owner is set to the current user, with permissions checked
by IsOwnerOrReadOnly. The SnapFriendshipDetail view enables retrieving,
updating, and deleting individual SnapFriendship instances, restricted
to the user's own friendships through the same permission class.
"""


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
