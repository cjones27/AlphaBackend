from ninja.security import APIKeyHeader
from users.models import User
from ninja.security import HttpBearer

class UserAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            return User.objects.get(api_key = token)
        except User.DoesNotExist:
            pass

class AdminAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            return User.objects.get(api_key = token, is_admin = 1)
        except User.DoesNotExist:
            pass