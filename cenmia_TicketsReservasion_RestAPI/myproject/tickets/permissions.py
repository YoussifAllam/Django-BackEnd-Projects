from rest_framework import permissions 

class IsAuther_OrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self , request , view , obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.Auther == request.user # will return True if user is auther 