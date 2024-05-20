from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from snap_comments.models import SnapComment

class SnapCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the SnapComment model
    Adds extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()
    attachment = serializers.FileField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created(self, obj):
        return naturaltime(obj.created)

    def get_updated(self, obj):
        return naturaltime(obj.updated)

    def validate_attachment(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Attachment size larger than 2MB!')
        if hasattr(value, 'image'):
            if value.image.height > 4096:
                raise serializers.ValidationError('Image height larger than 4096px!')
            if value.image.width > 4096:
                raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    class Meta:
        model = SnapComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'snap', 'created', 'updated', 'body', 'title', 'is_flagged',
            'pet_name', 'pet_age', 'pet_breed', 'attachment'
        ]

class SnapCommentDetailSerializer(serializers.ModelSerializer):
    snap = serializers.ReadOnlyField(source="snap.id")

    class Meta:
        model = SnapComment
        fields = '__all__'
