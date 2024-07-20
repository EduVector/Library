from rest_framework.serializers import ModelSerializer

from apps.blog.models import Article


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "name",
            "description",
            "image",
            "category",
            "tags",
            "author"
        )
