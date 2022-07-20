from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from polls.models import Poll


class PollsListView(View):

    def get(self, request):
        return render(request, 'polls/polls_list.html')


class PollDetailView(LoginRequiredMixin, View):

    def get(self, request, id=None):
        try:
            poll = Poll.objects.get(id=id)
            passed_poll = poll.passed.filter(user=self.request.user).exists()
        except Poll.DoesNotExist:
            return redirect('home')
        return render(request, 'polls/poll_detail.html', context={'poll': poll, 'passed': passed_poll})
