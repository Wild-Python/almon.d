from django.contrib import admin
from .models import CustomUserModel


@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_editable = ['is_active', 'is_superuser', 'is_staff']
    list_display = ('id', 'username', 'email', 'is_active', 'is_superuser', 'is_staff')
