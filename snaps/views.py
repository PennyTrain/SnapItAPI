from rest_framework import generics, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Snap
from .serializers import SnapSerializer
from snap_it.permissions import IsOwnerOrReadOnly

class SnapList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    The perform_create method associates the post with the logged-in user.
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
        'owner__friended__owner__profile',  # the owner's feed
        'snaplikes__owner__profile',        # the owner's liked snaps
        'snapdislikes__owner__profile',     # the owner's disliked snaps
        'owner__profile',                   # the owner's snaps
    ]
    search_fields = [
        'owner__username',
        'title',
        'pet_name',
        'pet_age',
        'pet_breed',
        'pet_type'
    ]
    ordering_fields = [
        'snaplikes_count',
        'snapdislikes_count',
        'snapcomments_count',
        'snaplikes__created',
        'snapdislikes__created',
        'pet_name',
        'pet_age',
        'pet_breed',
        'pet_type'
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


