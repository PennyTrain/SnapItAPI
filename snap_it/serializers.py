from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
"""
The CurrentUserSerializer extends UserDetailsSerializer
from dj_rest_auth.serializers to include additional fields
related to the user's profile. It adds read-only fields for
the profile ID and profile image URL, enhancing the serialized
representation of the current user with this profile information.
"""


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
