from rest_framework.generics import ListAPIView

from apps.blog.models import Category

from .serializer import CategoryListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
