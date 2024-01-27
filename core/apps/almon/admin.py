from django.contrib import admin
from .models import Almon


# Register your models here.


@admin.register(Almon)
class AlmonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'username',)
