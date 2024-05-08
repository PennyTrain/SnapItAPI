from rest_framework import filters, generics
from django.db.models import Count 
from .models import Profile
from .serializers import ProfileSerializer
from snap_it.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        snaps_count=Count('owner__snap', distinct=True),
        friended_count=Count('owner__friended', distinct=True),
        friendship_count=Count('owner__friended__friended', distinct=True)  # Access SnapFriendship through User
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'snaps_count',
        'friended_count',
        'friendship_count',
        'owner__friended__friended__created_at',  # Ordering by friendship creation date
        'owner__friended__created_at',  # Ordering by friended creation date
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        snaps_count=Count('owner__snap', distinct=True),
        friended_count=Count('owner__friended', distinct=True),
        friendship_count=Count('owner__friended__friended', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer