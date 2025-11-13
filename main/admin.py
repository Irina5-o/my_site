from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    list_filter = ('title',)
    search_fields = ('title', 'description')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'link')
        }),
    )
