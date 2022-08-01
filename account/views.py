import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from account.forms import RegisterUserForm, LoginUserForm

logger = logging.getLogger('views')


class HomePage(View):

    def get(self, request):
        return render(request, 'base.html')


class AccountLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginUserForm


class AccountLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('account:login')


class RegistrationView(View):

    def get(self, request):
        form = RegisterUserForm()
        if not self.request.user.is_authenticated:
            return render(request, 'registration/registration.html', {'form': form})
        return redirect('home')

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            logger.debug('create new user')
            messages.success(request, 'Поздравляем, регистрация завершена!')
            return redirect('home')
        else:
            return render(request, 'registration/registration.html', {'form': form})


class PlayersListView(LoginRequiredMixin, TemplateView):
    template_name = 'players/players_list.html'


class UserSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/settings.html'
