from django.conf import settings
from django.contrib.postgres.indexes import GinIndex, OpClass
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.functions import Upper
from django.urls import reverse


class Poll(models.Model):
    title = models.CharField('Наименование опроса', max_length=200, db_index=True)
    gain = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
        ],
        verbose_name='Награда за прохождение'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    @property
    def has_gain(self):
        return bool(self.gain)

    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-created_at', 'title']
        # indexes = [
        #     GinIndex(OpClass(Upper('title'), name='gin_trgm_ops'), name='title_upper_gin_index'),  # индекс для icontains
        # ]

    def __str__(self):
        return 'Опросник %s с вопросами в кол-ве %s штук' % (self.title, self.questions.all().count())


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Опрос',
                             related_name='questions')
    title = models.CharField('Наименование', max_length=400)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', related_name='choices')
    text = models.CharField(max_length=4096)

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class PassedPoll(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='polls')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='passed')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пройденный опрос'
        verbose_name_plural = 'Пройденные опросы'

    def __str__(self):
        return 'Опрос %s, пройден пользователем %s' % (self.poll, self.user)


class PollAnswerQuestions(models.Model):
    pool_answer = models.ForeignKey(PassedPoll, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer_for_question = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Ответ на пройденный опрос'
        verbose_name_plural = 'Ответы на пройденный опрос'

    def __str__(self):
        return f'{self.question}: {self.answer_for_question}'
