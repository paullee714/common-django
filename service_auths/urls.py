from django.urls import path
from rest_framework_simplejwt.views import (
    TokenVerifyView,
)

from service_auths.views import (
    TokenPairView,
    RefreshTokenPairView,
    VerifyMeView,
)

urlpatterns = [
    path(
        "token",
        TokenPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh",
        RefreshTokenPairView.as_view(),
        name="token_refresh",
    ),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("verify-me", VerifyMeView.as_view(), name="verify_me"),
]
