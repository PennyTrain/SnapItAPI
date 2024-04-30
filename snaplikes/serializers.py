from rest_framework import serializers
from .models import SnapLike

class SnapLikeSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SnapLike
        fields = ['id', 'created', 'owner', 'snap']