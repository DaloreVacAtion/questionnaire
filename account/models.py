from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    Black, White, WhiteSmoke, Silver, Gray, Green, Red, Yellow = ['#000000', '#FFFFFF', '#F5F5F5', '#C0C0C0',
                                                                  '#BEBEBE', '#008000', '#FF0000', '#FFFF00']
    COLORS = (
        (Black, 'Черный'),
        (White, 'Белый'),
        (WhiteSmoke, 'Белая дымка'),
        (Silver, 'Серебрянный'),
        (Gray, 'Серый'),
        (Green, 'Зеленый'),
        (Red, 'Красный'),
        (Yellow, 'Желтый')
    )

    username = models.CharField(
        'Имя пользователя',
        db_index=True,
        max_length=150,
        unique=True,
        error_messages={
            'unique': "Такое имя пользователя уже занято",
        }
    )
    background_color = models.CharField(verbose_name='Цвет заднего фона', choices=COLORS, default=White, max_length=128)
    username_color = models.CharField(verbose_name='Цвет ника', choices=COLORS, default=White, max_length=128)
    balance = models.PositiveIntegerField(verbose_name='Баланс', default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def add_gain_to_current_balance(self, gain: int):
        self.balance += gain
        self.save()

    def remove_gain_from_balance(self, gain: int):
        self.balance -= gain
        self.save()
