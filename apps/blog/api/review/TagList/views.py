from rest_framework.generics import ListAPIView

from apps.blog.models import Tag

from .serializer import TagListSerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
