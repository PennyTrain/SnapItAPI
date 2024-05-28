from rest_framework import serializers
from .models import Profile
from friendships.models import SnapFriendship
"""
The ProfileSerializer is a Django REST Framework serializer
for the Profile model, including fields such as owner, created_at,
updated_at, and pet-related information, with several fields
set to read-only. It includes custom methods to determine if
the requesting user is the profile owner (get_is_owner) and to
retrieve the friendship ID between the requesting user and the
profile owner (get_friendship_id). The serializer's meta class
specifies which fields to include in the serialized output.
"""


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    friendship_id = serializers.SerializerMethodField()
    friendship_count = serializers.ReadOnlyField()
    friended_count = serializers.ReadOnlyField()
    snaps_count = serializers.ReadOnlyField()
    pet_name = serializers.ReadOnlyField()
    pet_age = serializers.ReadOnlyField()
    pet_breed = serializers.ReadOnlyField()
    pet_type = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_friendship_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            friended = SnapFriendship.objects.filter(
                owner=user, friended=obj.owner
            ).first()
            return friended.id if friended else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'friendship_id',
            'snaps_count', 'friendship_count', 'friended_count', 'pet_name',
            'pet_age', 'pet_breed', 'pet_type'
        ]
