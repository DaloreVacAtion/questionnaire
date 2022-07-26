# Generated by Django 4.0.6 on 2022-07-19 17:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4096)),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
        migrations.CreateModel(
            name='PassedPoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Пройденный опрос',
                'verbose_name_plural': 'Пройденные опросы',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Наименование опроса')),
                ('gain', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Награда за прохождение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
                'ordering': ['-created_at', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Наименование')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.poll', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='PollAnswerQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_for_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.choice')),
                ('pool_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.passedpoll')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.question')),
            ],
            options={
                'verbose_name': 'Ответ на пройденный опрос',
                'verbose_name_plural': 'Ответы на пройденный опрос',
            },
        ),
        migrations.AddField(
            model_name='passedpoll',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passed', to='polls.poll'),
        ),
        migrations.AddField(
            model_name='passedpoll',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.question', verbose_name='Вопрос'),
        ),
    ]
