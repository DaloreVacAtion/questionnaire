from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from polls.models import Poll


class PollExistMixin(AccessMixin):
    """Verify that the poll is exist."""

    def dispatch(self, request, *args, **kwargs):
        poll_id = kwargs.get('id')
        try:
            Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
