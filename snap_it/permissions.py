from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    if request.method in permissions.SAFE_METHODS:
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
      return True
        # Write permissions are only allowed to the owner of the object.
    return obj.owner == request.user