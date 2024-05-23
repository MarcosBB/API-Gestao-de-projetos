from .models import Task, Project, Sprint
from rest_flex_fields import FlexFieldsModelSerializer
from auth_app.serializers import UserSerializer


class SprintSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Sprint
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "end_date",
        ]


class ProjectSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "is_active",
            "created_at",
            "updated_at",
            "customer",
        ]
        expandable_fields = {
            "customer": UserSerializer,
        }


class TaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "priority",
            "created_at",
            "updated_at",
            "project",
            "sprint",
            "reporter",
            "assignee",
            "status",
        ]
        expandable_fields = {
            "project": ProjectSerializer,
            "sprint": SprintSerializer,
            "reporter": UserSerializer,
            "assignee": UserSerializer,
        }
