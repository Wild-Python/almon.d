from django.contrib import admin
from .models import Almon, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Almon)
class AlmonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'username', 'category',)
