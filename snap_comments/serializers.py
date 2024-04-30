from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from snap_comments.models import SnapComment


class SnapCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()