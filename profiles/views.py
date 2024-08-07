from rest_framework import filters, generics
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from snap_it.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
"""
This code defines two API views for managing profiles using Django
REST Framework. The ProfileList view lists profiles with additional
annotations for counts of snaps, friends, and friendships, and
supports filtering and ordering based on various fields, including
pet attributes and friendship dates. The ProfileDetail view allows
retrieving and updating individual profiles, restricted by the
IsOwnerOrReadOnly permission, with the same annotations for
additional profile metrics.
"""


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        snaps_count=Count('owner__snap', distinct=True),
        friended_count=Count('owner__friended', distinct=True),
        friendship_count=Count('owner__friended__friended', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__friended__friended__profile'
    ]
    ordering_fields = [
        'snaps_count',
        'friended_count',
        'friendship_count',
        'owner__friended__friended__created_at',
        'owner__friended__created_at',
        'pet_type',
        'pet_breed',
        'pet_age',
        'pet_name',
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
