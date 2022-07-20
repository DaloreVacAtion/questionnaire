from django.urls import path
from .views import *

urlpatterns = [
    path('', PollsListView.as_view(), name='polls'),
    path('<int:id>/', PollDetailView.as_view(), name='poll_detail'),
]