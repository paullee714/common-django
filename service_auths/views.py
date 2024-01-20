from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from common.global_response import CommonResponse
from service_auths.serializer import (
    TokenCustomSerializer,
    RefreshTokenCustomSerializer,
)


class RefreshTokenPairView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RefreshTokenCustomSerializer


class TokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TokenCustomSerializer


class VerifyMeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return CommonResponse(
            data=[],
            res_status=status.HTTP_200_OK,
            message="this is good",
        )
