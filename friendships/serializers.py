from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SnapFriendship


class SnapFriendshipSerializer(serializers.ModelSerializer):
    """
The SnapFriendshipSerializer is a Django REST Framework
serializer for the SnapFriendship model, designed to handle
the serialization and deserialization of SnapFriendship instances.
It includes fields for the owner's and friended user's usernames,
ensuring these fields are read-only and derived from the respective
user objects. The create method overrides the default to allow
the creation of a SnapFriendship instance by fetching the User
object for the friended user based on the username provided in
the validated data, associating it with the owner derived from
the request's user context.
"""
    owner = serializers.ReadOnlyField(source='owner.username')
    friended_user = serializers.ReadOnlyField(source='friended.username')

    class Meta:
        model = SnapFriendship
        fields = ('id', 'owner', 'friended', 'created', 'friended_user')

    def create(self, validated_data):
        friended_data = validated_data.pop('friended')
        friended_user = User.objects.get(username=friended_data['username'])
        return SnapFriendship.objects.create(
                                            owner=self.context['request'].user,
                                            friended=friended_user
                                              )
