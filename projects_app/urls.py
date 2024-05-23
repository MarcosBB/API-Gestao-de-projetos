from rest_framework.routers import DefaultRouter

from .viewsets import TaskViewSet, ProjectViewSet, SprintViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")
router.register("projects", ProjectViewSet, basename="projects")
router.register("sprints", SprintViewSet, basename="sprints")

urlpatterns = router.urls
