from django.urls import path

from account.views import (
    RegistrationView, LoginView, LogoutView, PlayersListView, UserSettingsView,
)

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('settings/', UserSettingsView.as_view(), name='settings'),
    path('players/', PlayersListView.as_view(), name='players')
]
