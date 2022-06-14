from django.contrib import admin

from django.utils.translation import gettext, gettext_lazy as _
# models.pyで指定したクラス名
from .models import UserDB

admin.site.register(UserDB)

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'profile', 'icon', 'birthday', 'gender')}),
        (_('Personal Info',), {'fields': ('email',)}),
        (_('Permissions',), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Password',), {'fields': ('password_changed', 'password_changed_date',)}),
        (_('Important Dates',), {'fields': ('last_login', 'date_joined',)}),
    )

    list_display = ('uuid', 'username', 'email', 'is_active',)