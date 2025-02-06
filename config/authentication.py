from rest_framework.authentication import BaseAuthentication
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("X-USERNAME")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None) # tuple 형식으로 보내는 것이 규칙
        except User.DoesNotExist:
            raise AuthenticationFailed(f"No user with username {username}")


