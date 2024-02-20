from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication

class CustomAuthentication(BaseAuthentication):
  def authenticate(self, request):
    user = None
    username = request.query_params.get("username", None)

    if username is not None:
      try:
        user = User.objects.get(username=username)
      except User.DoesNotExist:
        raise AuthenticationFailed(f"User {username} not found")

      return (user, None)
    else:
      return None
