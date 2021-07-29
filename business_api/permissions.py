from rest_framework import permissions


class AccessOwnProfile(permissions.BasePermission):
    """allow business to access data he/she has been provided"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to their own data"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

"""
class UpdateOwnStatus(permissions.BasePermission):
    #Allow users to update their own status

    def has_object_permission(self, request, view, obj):
        #Check the user is trying to update their own status
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.business.id == request.user.id
"""


class AccessOwnFormPart(permissions.BasePermission):
    """Allow forms to update their own parts"""

    def has_object_permission(self, request, view, obj):
        """Check the form is trying to update their own part"""
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.form.id == request.form.id
