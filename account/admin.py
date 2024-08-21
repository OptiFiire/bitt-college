# from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ["id", "username", "user_groups", "email", "created_at", "updated_at"]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (
            None,
            {
                "fields": ("username", "email", "password", "last_login"),
            },
        ),
        (
            "Permissions",
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
    )
    
    def user_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    user_groups.short_description = 'Group'
    
    def save_model(self, request, obj, form, change):
        if not obj.password.startswith('pbkdf2_'):
            obj.password = make_password(obj.password)

        super().save_model(request, obj, form, change)

        if request.user == obj:
            update_session_auth_hash(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
