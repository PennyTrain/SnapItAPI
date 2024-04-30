from rest_framework import serializers
from .models import Snap


class SnapSerializer(serializers.ModelSerializer):
    """
    SnapSerializer class defines a serializer for the Snap model, 
    with fields such as owner, is_owner, profile_id, and profile_image.
    A custom method get_is_owner is used to determine if the 
    requesting user is the owner of the snap. Additionally, it contains a 
    validate_image method to validate the size and dimensions of the uploaded 
    image. Finally, the class Meta specifies the model and fields to include 
    in the serialization.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Snap
        fields = [
            'id', 'owner', 'is_owner',
            'profile_id', 'profile_image', 
            'created', 'updated', 'title', 
            'body', 'featured_image', 'status'
            ]
