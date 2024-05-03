from rest_framework import serializers
from .models import SnapFriendship
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class SnapFriendshipSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    friended = UserSerializer(read_only=True)

    class Meta:
        model = SnapFriendship
        fields = ('id', 'owner', 'friended', 'created')