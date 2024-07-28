from rest_framework.generics import RetrieveUpdateDestroyAPIView
from apps.common.permissions import IsAuthor

from apps.library.models import Book

from .serializer import BookRUDSerializer


class BookRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRUDSerializer
    permission_classes = [IsAuthor]
    lookup_field = "slug"

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return super().get_permissions()
