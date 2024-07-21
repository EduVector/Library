from rest_framework.serializers import ModelSerializer

from apps.blog.models import Tag


class TagCreateSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "name",
        )
