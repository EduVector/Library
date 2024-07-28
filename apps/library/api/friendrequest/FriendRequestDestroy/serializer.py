from rest_framework.serializers import ModelSerializer, ValidationError

from apps.library.models import FriendRequest


class FriendRequestDestroySerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "from_user",
            "to_user",
        )


