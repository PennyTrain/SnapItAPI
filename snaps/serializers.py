from rest_framework import serializers
from .models import Snap

class SnapSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Snap
        fields = ('id', 'owner', 'created', 'updated', 'title', 'body', 'featured_image', 'status')
        