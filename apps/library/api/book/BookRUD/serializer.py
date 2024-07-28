from rest_framework.serializers import ModelSerializer

from apps.library.models import Book
from apps.user.api.CustomUser.serializer import UserSerializer


class BookRUDSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            "name",
            "slug",
            "author",
            "description",
            "genres",
            "published_at",
            "pages",
            "award",
            "cover",
            "created_at",
        )
        extra_kwargs = {
            "published_at": {"read_only": True},
            "created_at": {"read_only": True}
        }
