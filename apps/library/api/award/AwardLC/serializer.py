from rest_framework.serializers import ModelSerializer

from apps.library.models import Award


class AwardListCreateSerializer(ModelSerializer):
    class Meta:
        model = Award
        fields = (
            "id",
            "name",
            "date",
        )
