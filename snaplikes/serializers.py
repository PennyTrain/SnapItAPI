from rest_framework import serializers
from .models import SnapLike
from django.db import IntegrityError
"""
The SnapLikeSerializer is a Django REST Framework serializer for
the SnapLike model, including fields for ID, creation timestamp,
owner username, and snap. It overrides the create method to handle
IntegrityError exceptions, raising a validation error with a message
indicating a possible duplicate entry.
"""


class SnapLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SnapLike
        fields = ['id', 'created', 'owner', 'snap']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
