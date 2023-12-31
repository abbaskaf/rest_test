from rest_framework import permissions
from django.contrib.auth.models import User


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(username=request.query_params['username'])
        except:
            return False
        if user.is_superuser:
            return True
        if not request.user == user:
            return False
        else:
            return True
