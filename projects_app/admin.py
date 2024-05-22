from django.contrib import admin

from .models import Task, Project, Sprint

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "sprint", "created_at")
    list_filter = ("priority", "project", "sprint", "reporter", "assignee")
    search_fields = ("name", "description")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "customer", "is_active", "created_at")
    list_filter = ("customer", "is_active")
    search_fields = ("name", "description")


class SprintAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")
    search_fields = ("name", "description")


admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Sprint, SprintAdmin)