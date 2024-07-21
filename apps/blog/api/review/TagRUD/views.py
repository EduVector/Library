from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.blog.models import Tag

from .serializer import TagRUDSerializer


class TagRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagRUDSerializer
    lookup_field = 'slug'
