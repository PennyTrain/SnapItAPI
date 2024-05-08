from rest_framework import serializers
from .models import Profile
from friendships.models import SnapFriendship


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    friendship_id = serializers.SerializerMethodField()
    friendship_count = serializers.ReadOnlyField()
    friended_count = serializers.ReadOnlyField()
    snaps_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_friendship_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            friendship = SnapFriendship.objects.filter(
                owner=user, friended=obj.owner
            ).first()
            return friendship.id if friendship else None
        return None 

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'friendship_id', 
            'snaps_count', 'friendship_count', 'friended_count'
        ]