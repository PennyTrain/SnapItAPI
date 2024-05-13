from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .settings import (JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE)
from django.http import JsonResponse
from datetime import datetime

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my API, used for the Snap it Application!"
    })

# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    """
    View function for logging out users by expiring authentication tokens.
    Handles POST requests and returns a JSON response.
    """
    response = JsonResponse({})
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires=datetime(1970, 1, 1),
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires=datetime(1970, 1, 1),
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response