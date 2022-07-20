import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from account.forms import RegisterUserForm
from account.models import User

logger = logging.getLogger('views')


class HomePage(View):

    def get(self, request):
        return render(request, 'base.html')


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        logger.debug(f'user with username {username} try to connect')
        if username == '' or password == '':
            messages.success(request,
                             ('Поля "username/password" не могут быть пустыми. Пожалуйста, попробуйте снова...'))
            return redirect('account:login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                logger.debug(f'user {username} connect to the admin area')
                return redirect('/admin/')
            next_page = request.POST.get('next', 'home')
            logger.debug(f'find some next parameter {next_page}')
            if next_page:
                return redirect(request.POST.get('next', 'home'))
            return redirect('home')
        else:
            if User.objects.filter(username=username).exists():
                messages.success(request, ('Произошла ошибка входа. Пожалуйста, проверьте пароль...'))
            else:
                messages.success(request, ('Пользователя с таким username не существует'))
            return redirect('account:login')


class LogoutView(View):

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


class PlayersListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'players/players_list.html')


class UserSettingsView(View):
    def get(self, request):
        return render(request, 'registration/settings.html')
