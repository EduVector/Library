from rest_framework.generics import CreateAPIView

from apps.blog.models import Tag

from .serializer import TagCreateSerializer


class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateSerializer
