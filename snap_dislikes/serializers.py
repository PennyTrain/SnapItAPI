from rest_framework import serializers
from .models import SnapDislike
from django.db import IntegrityError

class SnapDislikeSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source='owner.username')

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