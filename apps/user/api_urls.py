from django.urls import path

from apps.user.api.UserRegister.views import UserRegisterCreateView


app_name = "user"

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name="register")
]