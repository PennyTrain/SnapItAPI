from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from snap_it.permissions import IsOwnerOrReadOnly
from .models import SnapComment
from .serializers import SnapCommentSerializer, SnapCommentDetailSerializer


class SnapCommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = SnapCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SnapComment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_field = [
        'snap'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnapCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SnapCommentDetailSerializer
    queryset = SnapComment.objects.all()