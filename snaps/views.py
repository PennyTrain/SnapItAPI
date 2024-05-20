from rest_framework import generics, filters
from django.db.models import Count
from .models import Snap
from .serializers import SnapSerializer
from snap_it.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class SnapList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = SnapSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Snap.objects.annotate(
        snaplikes_count=Count('snaplikes', distinct=True),
        snapdislikes_count=Count('snapdislikes', distinct=True),
        snapcomments_count=Count('snapcomments', distinct=True)
    ).order_by('-created')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # the owners feed
        'owner__friended__owner__profile',
        # the owners liked snaps
        'snaplikes__owner__profile',
        # the owners disliked snaps
        'snapdislikes__owner__profile',
        # the owners snaps
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title'
        'pet_name'
        'pet_age'
        'pet_breed'
    ]
    ordering_fields = [
        'snaplikes_count',
        'snapdislikes_count',
        'snapcomments_count',
        'snaplikes__created',
        'snapdislikes__created'
        'pet_name',
        'pet_age',
        'pet_breed',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    


class SnapDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = SnapSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Snap.objects.annotate(
        snaplikes_count=Count('snaplikes', distinct=True),
        snapdislikes_count=Count('snapdislikes', distinct=True),
        snapcomments_count=Count('snapcomments', distinct=True)
    ).order_by('-created')


