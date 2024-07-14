import random

from rest_framework.generics import CreateAPIView, GenericAPIView

from rest_framework import status
from rest_framework.response import Response

from apps.user.models import User, VerifyEmail

from .serializer import UserRegisterSerializer

from apps.user.utils import Util


class UserRegisterCreateView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            exists_user = User.objects.filter(email=email).first()
            if exists_user and exists_user.is_verified:
                    return Response(
                        {"error": "Already registered with this email! Please sign in"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            code = str(random.randint(100_000, 999_999))
            data = {
                "to_email": email,
                "email_subject": "Check your verifiy code",
                "email_body": f"This is your {code} verifiy code!"
            }
            Util.send_email(data=data)
            VerifyEmail.objects.create(email=email, code=code)
            serizlizer = self.serializer_class(data=request.data)
            serizlizer.is_valid(raise_exception=True)
            serizlizer.save()
            return Response({'success': True, 'message': 'Please verify Email'},
                                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                 {
                      "error": f"{e}"
                 }, status=status.HTTP_400_BAD_REQUEST
            )






