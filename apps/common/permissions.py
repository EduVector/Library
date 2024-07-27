from rest_framework.permissions import IsAuthenticated


class IsAuthor(IsAuthenticated):
    """
        Allows access only to author users.
    """
    def has_permission(self, request, view):
        return bool(request.user.is_author and request.user.is_authenticated)
