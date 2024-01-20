from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from service_auths.models import MyServiceUserModel


from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthTests(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = MyServiceUserModel.objects.create_user(
            nickname="test_user",
            email="test_user@mail.com",
            password="qwerqwer123",
        )

        # URL for obtaining tokens
        self.token_url = reverse("token_obtain_pair")

        # URL for a protected view (change this to your view)
        self.protected_url = reverse("verify_me")

    def test_token_obtain(self):
        # Test token obtain
        response = self.client.post(
            self.token_url, {"nickname": "test_user", "password": "qwerqwer123"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.get("data"))
        self.assertTrue("refresh" in response.data.get("data"))

    def test_token_refresh(self):
        # Test token refresh
        refresh = RefreshToken.for_user(self.user)
        response = self.client.post(reverse("token_refresh"), {"refresh": str(refresh)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.get("data"))
        self.assertTrue("refresh" in response.data.get("data"))

    def test_protected_view_access(self):
        # Test access to a protected view
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer "
            + str(RefreshToken.for_user(self.user).access_token)
        )
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test access with invalid token
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + "invalidtoken")
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
