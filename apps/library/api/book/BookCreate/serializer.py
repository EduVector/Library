from rest_framework.serializers import ModelSerializer

from apps.library.models import Book

from apps.user.api.CustomUser.serializer import UserSerializer


class BookCreateSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            "name",
            "description",
            "author",
            "genres",
            "published_at",
            "pages",
            "award",
            "cover",
        )
