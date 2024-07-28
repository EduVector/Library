from rest_framework.serializers import ModelSerializer

from apps.library.models import Book

from apps.user.api.CustomUser.serializer import UserSerializer
from apps.library.api.genre.GenreLC.serializer import GenreLCSerializer
from apps.library.api.award.AwardLC.serializer import AwardListCreateSerializer


class BookListSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    genres = GenreLCSerializer(many=True)
    award = AwardListCreateSerializer(many=True)

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
