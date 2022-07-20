import logging

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from account.models import User
from api.exceptions import BadRequest
from api.filters import PollFilter
from api.pagination import DefaultPaginationResult
from api.serializers import PollDetailSerializer, PollsListSerializer, CreateOrUpdatePollAnswerSerializer, \
    UpdateUserColors, PlayersListSerializer
from polls.models import Poll, PassedPoll

logger = logging.getLogger('api')


class PollViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollDetailSerializer
    pagination_class = DefaultPaginationResult
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PollFilter
    serializer_action_classes = {
        'list': PollsListSerializer,
    }

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class SetPollAnswerApiView(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           generics.GenericAPIView):
    serializer_class = CreateOrUpdatePollAnswerSerializer
    permission_classes = (IsAuthenticated,)

    poll = None

    def get_object(self):
        try:
            return PassedPoll.objects.get(user=self.request.user, poll=self.poll)
        except Poll.DoesNotExist:
            raise BadRequest(detail='not a single passed polls was found')

    def post(self, request, *args, **kwargs):
        self.poll = self.request.data.get('poll')
        if self.poll is None:
            raise BadRequest(detail='poll is required param for update or create passed polls')

        if PassedPoll.objects.filter(user=self.request.user, poll=self.poll).exists():
            logger.debug(f'update poll answers for user {self.request.user.username} and poll with id {self.poll}')
            return super().update(request, partial=True)
        logger.debug(f'create poll answers for user {self.request.user.username} and poll with id {self.poll}')
        return super().create(request)


class SetNewColorsForUserApiView(mixins.UpdateModelMixin,
                                 generics.GenericAPIView):
    serializer_class = UpdateUserColors

    def get_object(self):
        return self.request.user

    def post(self, request):
        return self.update(request, partial=True)


class PlayersListViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = User.objects.filter(is_staff=False, is_superuser=False).annotate(passed_polls=Count('polls'))
    serializer_class = PlayersListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = DefaultPaginationResult
