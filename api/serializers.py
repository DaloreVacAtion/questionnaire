from rest_framework import serializers, status

from account.models import User
from api.decorators import query_debugger
from api.exceptions import PaymentError
from polls.models import Poll, Question, Choice, PassedPoll, PollAnswerQuestions


class PollsListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H-%M')
    url = serializers.URLField(source='get_absolute_url')

    class Meta:
        model = Poll
        fields = ['title', 'has_gain', 'url', 'gain', 'created_at']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['text']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['choices']


class PollDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H-%M')
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['created_at', 'title', 'questions']


class PollAnswerQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollAnswerQuestions
        fields = ['question', 'answer_for_question']


class CreateOrUpdatePollAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    answers = PollAnswerQuestionsSerializer(many=True)

    class Meta:
        model = PassedPoll
        fields = ['poll', 'user', 'answers']

    def create(self, validated_data):
        passed_poll = PassedPoll.objects.create(
            user=validated_data['user'],
            poll=validated_data['poll']
        )
        passed_poll.save()
        answers = [
            PollAnswerQuestions(
                pool_answer=passed_poll,
                question=answer['question'],
                answer_for_question=answer['answer_for_question']
            )
            for answer in validated_data['answers']
        ]
        PollAnswerQuestions.objects.bulk_create(answers)
        passed_poll.user.add_gain_to_current_balance(passed_poll.poll.gain)
        return passed_poll

    def update(self, instance, validated_data):
        instance.answers.all().delete()
        answers = [
            PollAnswerQuestions(
                pool_answer=instance,
                question=answer['question'],
                answer_for_question=answer['answer_for_question']
            )
            for answer in validated_data['answers']
        ]
        PollAnswerQuestions.objects.bulk_create(answers)
        return instance


class ColorChoiceField(serializers.ChoiceField):

    def to_representation(self, data):
        if data not in self.choices.keys():
            self.fail('invalid_choice', input=data)
        else:
            return self.choices[data]

    def to_internal_value(self, data):
        for key, value in self.choices.items():
            if key == data:
                return key
        self.fail('invalid_choice', input=data)


class UpdateUserColors(serializers.ModelSerializer):
    username_color = ColorChoiceField(choices=User.COLORS)
    background_color = ColorChoiceField(choices=User.COLORS)

    class Meta:
        model = User
        fields = ['username_color', 'background_color']

    def update(self, instance, validated_data):
        if instance.balance < 100:
            raise PaymentError("У вас слишком мало Валюты! Попробуйте пройти пару опросов.")
        instance.remove_gain_from_balance(100)
        return super().update(instance, validated_data)


class PlayersListSerializer(serializers.ModelSerializer):
    passed_polls = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'passed_polls', 'username_color', 'background_color']
