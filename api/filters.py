from django_filters import rest_framework as filters
from polls.models import Poll


class PollFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Poll
        fields = ['title']
