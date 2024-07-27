from django.urls import path

from .api.award.AwardLC.views import AwardListCreateView
from .api.award.AwardRUD.views import AwardRetrieveUpdateDestroyView

from .api.book.BookCreate.views import BookCreateView

app_name = "library"

urlpatterns = [
    path("Award/", AwardListCreateView.as_view(), name="award_list_create"),
    path("Award/<int:pk>/", AwardRetrieveUpdateDestroyView.as_view(), name="award_retrieve_update_destroy"),

    path("BookCreate/", BookCreateView.as_view(), name="book_create"),
]
