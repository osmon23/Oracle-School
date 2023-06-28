from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Teacher, Student


class TeacherAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'phone_number',
        'username',
        'first_name',
        'last_name',
        'grade',
        'subject',
    )
    list_display_links = (
        'phone_number',
    )
    search_fields = (
        'username',
        'phone_number',
    )
    fieldsets = (
        (None, {"fields": ("phone_number", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "grade", "subject")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Teacher, TeacherAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'date_of_birth',
        'grade',
        'address',
        'gender',
        'photo',
    )
    list_display_links = (
        'full_name',
    )
    search_fields = (
        'full_name',
        'email',
        'gender',
    )
