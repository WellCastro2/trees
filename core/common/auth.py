from django.contrib.auth.backends import ModelBackend
from core.models import User


class ProxiedModelBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
