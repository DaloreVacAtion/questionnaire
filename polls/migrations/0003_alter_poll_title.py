# Generated by Django 4.0.6 on 2022-07-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_poll_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Наименование опроса'),
        ),
    ]
