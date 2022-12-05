from rest_framework import permissions

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
   def has_permission(self, request, view):
       if request.method == 'POST':
           return True
       return super(IsAuthenticatedOrCreate, self).has_permission(request, view)

class CustomReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email       