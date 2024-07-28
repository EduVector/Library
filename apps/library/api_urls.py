from django.urls import path

from .api.award.AwardLC.views import AwardListCreateView
from .api.award.AwardRUD.views import AwardRetrieveUpdateDestroyView

from .api.book.BookCreate.views import BookCreateView
from .api.book.BookList.views import BookListView
from .api.book.BookRUD.views import BookRUDView

from .api.friendrequest.FriendRequestCreate.views import FriendRequestCreateView
from .api.friendrequest.FriendRequestRetrieve.views import MyFriendsView
from .api.friendrequest.FriendRequestDestroy.views import FriendRequestDestroyView

app_name = "library"

urlpatterns = [
    path("Award/", AwardListCreateView.as_view(), name="award_list_create"),
    path("Award/<int:pk>/", AwardRetrieveUpdateDestroyView.as_view(), name="award_retrieve_update_destroy"),

    path("BookCreate/", BookCreateView.as_view(), name="book_create"),
    path("BookList/", BookListView.as_view(), name="book_list"),
    path("BookRUD/<slug:slug>/", BookRUDView.as_view(), name="book_retrieve_update_destroy"),

    path("FriendRequestCreate/", FriendRequestCreateView.as_view(), name="friend_request_create"),
    path("MyFriends/", MyFriendsView.as_view(), name="my_friends"),
    path("UnfollowFriend/<int:pk>/", FriendRequestDestroyView.as_view(), name="unfollow_friend")
]
