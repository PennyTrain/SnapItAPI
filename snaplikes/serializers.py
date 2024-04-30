from rest_framework import serializers
from .models import SnapLike
from django.db import IntegrityError

class SnapLikeSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source='owner.username')

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