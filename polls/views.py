from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from polls.mixins import PollExistMixin
from polls.models import Poll


class PollsListView(TemplateView):
    template_name = 'polls/polls_list.html'


class PollDetailView(LoginRequiredMixin, PollExistMixin, TemplateView):
    template_name = 'polls/poll_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PollDetailView, self).get_context_data(**kwargs)
        poll = Poll.objects.get(id=kwargs.get('id'))
        context['poll'] = poll
        context['passed_poll'] = poll.passed.filter(user=self.request.user).exists()
        return context
