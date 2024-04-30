from rest_framework import generics, permissions
from snap_it.permissions import IsOwnerOrReadOnly
from snaplikes.models import SnapLike
from .serializers import SnapLikeSerializer
from django.http import Http404

# Create your views here.

class SnapLikeList(generics.ListCreateAPIView):
    """
    Handles both listing and creation of SnapLike. 
    It sets the serializer class to SnapLikeSerializer,
    defines the queryset to retrieve all SnapLikes, and 
    makes sure that only authenticated users can create new 
    likes by assigning the owner of the like to the current 
    authenticated user during creation.
    """
    serializer_class = SnapLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SnapLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnapLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Used for retrieving and deleting individual SnapLikes. Making sure
    that only the owner of the like or a read-only request can perform 
    operations on the like instance by applying the IsOwnerOrReadOnly 
    permission class and checking object permissions before allowing access.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SnapLikeSerializer
    
    def get_object(self, pk):
        try:
            snaplike = SnapLike.objects.get(pk=pk)
            self.check_object_permissions(self.request, snaplike)
            return snaplike
        except SnapLike.DoesNotExist:
            raise Http404