from django.urls import path

from api.views import SetNewColorsForUserApiView, SetPollAnswerApiView

app_name = 'api'
urlpatterns = [
    path('colors/', SetNewColorsForUserApiView.as_view(), name='set_new_colors_for_user'),
    path('answers/', SetPollAnswerApiView.as_view(), name='answers'),
]
