from rest_framework.serializers import ModelSerializer

from apps.blog.models import Tag


class TagListSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "slug",
        )
