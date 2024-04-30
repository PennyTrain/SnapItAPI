from rest_framework import generics, permissions
from snap_it.permissions import IsOwnerOrReadOnly
from snaplikes.models import Like
from .serializers import LikeSerializer
from django.http import Http404

# Create your views here.

class SnapLikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    
    def get_object(self, pk):
        try:
            like = Like.objects.get(pk=pk)
            self.check_object_permissions(self.request, like)
            return like
        except Like.DoesNotExist:
            raise Http404