from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_flex_fields import FlexFieldsModelViewSet
from .models import Project, Sprint, Task
from .serializers import ProjectSerializer, SprintSerializer, TaskSerializer


class TaskViewSet(FlexFieldsModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["project", "sprint", "reporter", "assignee"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "priority", "id"]
    ordering = ["-created_at"]
    permit_list_expands = ["project", "sprint", "reporter", "assignee"]
