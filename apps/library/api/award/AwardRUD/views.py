from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.library.models import Award

from .serializer import AwardRUDteSerializer


class AwardRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardRUDteSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
