from apps.user.api.CustomUser.serializer import UserSerializer
from apps.blog.api.category.CategoryList.serializer import CategoryListSerializer
from apps.blog.api.tag.TagList.serializer import TagListSerializer
from apps.blog.models import Article
from rest_framework.serializers import ModelSerializer


class ArticleListSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategoryListSerializer(read_only=True)
    tags = TagListSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "image",
            "category",
            "tags",
            "author"
        )
