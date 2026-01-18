from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models


class UserAdmin(BaseUserAdmin):
    """Manage user in the admin site."""
    list_display = ["email", "name", "is_staff"]
    ordering = ["email"]

admin.site.register(models.User, UserAdmin)



