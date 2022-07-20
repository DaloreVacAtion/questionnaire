from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm
from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ['username']
    ordering = ['username']
    search_fields = ['username']
    search_help_text = 'Имя пользователя'
    fieldsets = (
        ('Личная информация', {'fields': ('username', 'password', 'balance')}),
        (_('Permissions'), {
            'fields': ('is_active',
                       'is_staff',
                       'is_superuser',
                       'groups',
                       'user_permissions',
                       ),
        }),
        ('Цвета', {'fields': ('background_color', 'username_color')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
