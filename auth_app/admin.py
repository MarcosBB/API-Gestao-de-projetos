from django.contrib import admin
from .models import Customer, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "main_email")
    search_fields = ("name", "main_email")


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("username", "email", "is_staff", "is_customer")
    search_fields = ("username", "email")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "customer",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

    def is_customer(self, obj):
        return obj.customer is not None


admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)
