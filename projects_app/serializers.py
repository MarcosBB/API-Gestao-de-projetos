from .models import Task, Project, Sprint
from rest_flex_fields import FlexFieldsModelSerializer
from auth_app.serializers import UserSerializer, CustomerSerializer
from rest_framework import serializers


class SprintSerializer(FlexFieldsModelSerializer):
    tasks_count = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "end_date",
            "tasks_count",
        ]

    def get_tasks_count(self, obj):
        return obj.tasks.count()

    def validate(self, attrs):
        start_date = attrs.get("start_date") or (
            self.instance.start_date if self.instance else None
        )
        end_date = attrs.get("end_date") or (
            self.instance.end_date if self.instance else None
        )
        
        if start_date > end_date:
            raise serializers.ValidationError("Start date must be before end date")
        return super().validate(attrs)


class ProjectSerializer(FlexFieldsModelSerializer):
    tasks_count = serializers.SerializerMethodField()

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
            "tasks_count",
        ]
        expandable_fields = {
            "customer": CustomerSerializer,
        }

    def get_tasks_count(self, obj):
        return obj.tasks.count()


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
