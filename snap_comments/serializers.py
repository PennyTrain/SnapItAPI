from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from snap_comments.models import SnapComment

class SnapCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user == obj.owner
        return False

    def get_created(self, obj):
        return naturaltime(obj.created)

    def get_updated(self, obj):
        return naturaltime(obj.updated)

    class Meta:
        model = SnapComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'snap', 'created', 'updated', 'body', 'title', 'is_flagged',
            'pet_name', 'pet_age', 'pet_breed', 'attachment', 'pet_type'
        ]


class SnapCommentDetailSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='snap.id')