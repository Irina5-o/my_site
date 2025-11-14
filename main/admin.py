from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'has_video')
    search_fields = ('title', 'description')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'link')
        }),
        ('Видео демонстрация', {
            'fields': ('video', 'video_url'),
            'description': 'Загрузите видео файл или укажите ссылку на видео'
        }),
    )