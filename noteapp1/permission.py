from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    AllowAny
    )


class IsOwner(BasePermission):
    message = 'you must owner'
    # safe_method = ['PUT']

    # def has_permission(self, request, view):
    #     if request.method in self.safe_method:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


'''class IsLogin(AllowAny):
    message = 'not permit'

    def has_permission(self, request, view):
        if request.user is None:
            return True
        return False
'''