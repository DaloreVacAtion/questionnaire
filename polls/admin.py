from django import forms
from django.contrib import admin

from polls.models import Poll, Choice, Question, PassedPoll, PollAnswerQuestions


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['poll', 'title']}), ]
    inlines = [ChoiceInLine]


@admin.register(PassedPoll)
class PollAnswerAdmin(admin.ModelAdmin):
    pass


class PollAnswerQuestionsAdminForm(forms.ModelForm):
    class Meta:
        model = PollAnswerQuestions
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PollAnswerQuestionsAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['answer_for_question'].queryset = Choice.objects.filter(question=self.instance.question)


# Добавил это поле, чтобы при редактировании не возникало проблем с поиском ответа, например.
# Не знаю, зачем, но так кажется удобнее
@admin.register(PollAnswerQuestions)
class PollAnswerQuestionsAdmin(admin.ModelAdmin):
    form = PollAnswerQuestionsAdminForm
