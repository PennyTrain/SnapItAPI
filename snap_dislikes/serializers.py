from rest_framework import serializers
from .models import SnapDislike
from django.db import IntegrityError
"""
The code defines a serializer called SnapDislikeSerializer
using Django REST Framework for serializing and deserializing
SnapDislike instances. It includes the id, created, owner,
and snap fields, with the owner field set as read-only and
sourced from the owner's username. The create method overrides
the default behavior to catch potential IntegrityError exceptions,
indicating a possible duplicate entry, and raises a ValidationError
with a corresponding detail message if such an error occurs.
"""


class SnapDislikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SnapDislike
        fields = ['id', 'created', 'owner', 'snap']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
