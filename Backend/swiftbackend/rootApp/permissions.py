from rest_framework import permissions


class IsTaker(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if obj.role == 'Ride Taker':
            return True
