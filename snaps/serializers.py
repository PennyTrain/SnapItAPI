from rest_framework import serializers
from .models import Snap
from snaplikes.models import SnapLike
from snap_dislikes.models import SnapDislike
"""
The SnapSerializer is a Django REST Framework serializer for
the Snap model, including fields for the owner's username and
profile details, timestamps, and various snap attributes. It
includes computed fields for the current user's like and dislike
IDs on the snap, counts of likes, dislikes, and comments, and a
method to check if the current user is the owner. Additionally,
it provides validation to ensure that the uploaded image meets
size and dimension constraints.
"""


class SnapSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    snaplike_id = serializers.SerializerMethodField()
    snaplikes_count = serializers.ReadOnlyField()
    snapdislike_id = serializers.SerializerMethodField()
    snapdislikes_count = serializers.ReadOnlyField()
    snapcomments_count = serializers.ReadOnlyField()

    def get_snaplike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            snaplikes = SnapLike.objects.filter(
                owner=user, snap=obj
            ).first()
            return snaplikes.id if snaplikes else None
        return None

    def get_snapdislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            snapdislikes = SnapDislike.objects.filter(
                owner=user, snap=obj
            ).first()
            return snapdislikes.id if snapdislikes else None
        return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!')
        return value

    class Meta:
        model = Snap
        fields = [
            'id', 'owner', 'is_owner',
            'profile_id', 'profile_image',
            'created', 'updated', 'title',
            'body', 'featured_image', 'status',
            'snaplike_id', 'snaplikes_count',
            'snapdislike_id', 'snapdislikes_count',
            'snapcomments_count',
            'pet_name', 'pet_age', 'pet_breed',
            'event_date', 'location', 'pet_type'
        ]
