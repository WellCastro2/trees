from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class IsPlantedMixin(AccessMixin):
    """ if user is owner post ok else denied. """

    def dispatch(self, request, *args, **kwargs):
        """
        only user created planted
        """
        if self.get_object().user == self.request.user:
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied('Permission denied')
