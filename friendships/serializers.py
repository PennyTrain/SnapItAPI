from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SnapFriendship


class SnapFriendshipSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    friended = serializers.ReadOnlyField(source='friended.username')

    class Meta:
        model = SnapFriendship
        fields = ('id', 'owner', 'friended', 'created')

    def create(self, validated_data):
        friended_data = validated_data.pop('friended')
        friended_user = User.objects.get(username=friended_data['username'])
        return SnapFriendship.objects.create(owner=self.context['request'].user,
                                              friended=friended_user)
