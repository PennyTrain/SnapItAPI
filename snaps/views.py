from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Snap
from .serializers import SnapSerializer
from snap_it.permissions import IsOwnerOrReadOnly

# Create your views here.

class SnapList(APIView):
    """
    List of all the posts
    """
    def get(self, request):
        snaps = Snap.objects.all()
        serializer = SnapSerializer(
            snaps, many=True, context={'request', request}
        )
        return Response(serializer.data)
    

# class SnapDetail(APIView):
#     serializer_class = SnapSerializer
#     permission_class = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             snaps = Snap.objects.get(pk=pk)
#             self.check_object_permissions(self.request, snaps)
#             return snaps
#         except Snap.DoesNotExist:
#             raise Http404
        
        






