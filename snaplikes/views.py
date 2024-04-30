from rest_framework import generics, permissions
from snap_it.permissions import IsOwnerOrReadOnly
from snaplikes.models import SnapLike
from .serializers import SnapLikeSerializer
from django.http import Http404

# Create your views here.

class SnapLikeList(generics.ListCreateAPIView):
    serializer_class = SnapLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SnapLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnapLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SnapLikeSerializer
    
    def get_object(self, pk):
        try:
            snaplike = SnapLike.objects.get(pk=pk)
            self.check_object_permissions(self.request, snaplike)
            return snaplike
        except SnapLike.DoesNotExist:
            raise Http404