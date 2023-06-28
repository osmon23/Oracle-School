from django.contrib import admin

from .models import Grade, School


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'teacher',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'teacher',
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
    )
