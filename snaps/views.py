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
    List of all the snaps
    """

    def get(self, request):
        snaps = Snap.objects.all()
        serializer = SnapSerializer(
            snaps, many=True, context={'request', request}
        )
        return Response(serializer.data)


class SnapDetail(APIView):
    serializer_class = SnapSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_snap(self, pk):
        try:
            snap = Snap.objects.get(pk=pk)
            self.check_object_permissions(self.request, snap)
            return snap
        except Snap.DoesNotExist:
            raise Http404

    def get_object(self, request, pk):
        snap = self.get_object(pk)
        serializer = SnapSerializer(
            snap, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        snap = self.get_object(pk)
        serializer = SnapSerializer(
            snap, 
            data=request.data, 
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
        