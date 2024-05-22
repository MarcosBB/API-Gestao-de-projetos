from django.contrib import admin
from .models import Customer, User

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "main_email")
    search_fields = ("name", "main_email")

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_customer")
    search_fields = ("username", "email")
    
    def is_customer(self, obj):
        return obj.customer is not None


admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)