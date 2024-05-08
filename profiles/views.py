from rest_framework import filters, generics
from django.db.models import Count 
from .models import Profile
from .serializers import ProfileSerializer
from snap_it.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        snaps_count=Count('owner__snap', distinct=True),
        friended_count=Count('owner__friended', distinct=True),
        # following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'snaps_count',
        'friended_count',
        # 'following_count',
        # 'owner__following__created_at',
        'owner__friended__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        snaps_count=Count('owner__snap', distinct=True),
        friended_count=Count('owner__friended', distinct=True),
        # following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer