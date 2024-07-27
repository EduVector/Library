from rest_framework.generics import ListCreateAPIView

from apps.library.models import Award

from .serializer import AwardListCreateSerializer


class AwardListCreateView(ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardListCreateSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True).order_by("-date__year")
