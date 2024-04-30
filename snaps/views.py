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
        """
        This retrieves a Snap from the database 
        based on the provided primary key and checks the 
        permissions using the check_object_permissions method. 
        If the Snap does not exist, it raises a Http404 exception.
        """
        try:
            snap = Snap.objects.get(pk=pk)
            self.check_object_permissions(self.request, snap)
            return snap
        except Snap.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        This get retrieves a Snap based on the provided primary key
        and serializes it using the SnapSerializer, ensuring the request context 
        is included. It then returns the serialized data in the response.
        """
        snap = self.get_snap(pk)
        serializer = SnapSerializer(
            snap, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        # """  
        # This put method first retrieves a Snap instance based on the 
        # provided primary key. Then initializes a SnapSerializer 
        # with the retrieved instance and the data from the request, 
        # ensuring the request context is included. 
        # If the serializer validates the data successfully, it saves 
        # the updated instance and returns the serialized data in the response. 
        # If there are validation errors, it returns an error response with 
        # the serializer errors and a status code indicating a bad request.
        # """
        snap = self.get_snap(pk)
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
    
    