from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .settings import (JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE)

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my API, used for the Snap it Application!"
    })

# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    """
    This code defines a view function for logging out users.
    It handles POST requests, where it creates a response object.
    Then, it sets two cookies (JWT_AUTH_COOKIE and JWT_AUTH_REFRESH_COOKIE) 
    with empty values and specific attributes like expiration, security settings,
    and same-site policy to ensure secure logout. Finally, it returns 
    the response object with the updated cookies to the client, effectively
    logging the user out by expiring their authentication tokens.
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response