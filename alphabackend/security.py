from ninja.security import APIKeyHeader
from users.models import User
from ninja.security import HttpBearer

class AnyUserApiKey(APIKeyHeader):

    # Request header name defined as api-key
    param_name = "api-key"

    def authenticate(self, request, key):
        # header value is stored in the key parameter
        try:
            # retrieve current user using indexed column api_key
            current_user = User.objects.get(api_key=key)

            # return value can be retrieved from routes accessing request.auth
            return current_user

        except User.DoesNotExist:

            # No return value implies { detail: Unauthorized } respones
            return

class UserAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            return User.objects.get(api_key = token)
        except User.DoesNotExist:
            pass

class AdminAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            return User.objects.get(api_key = token, user_type = 1)
        except User.DoesNotExist:
            pass