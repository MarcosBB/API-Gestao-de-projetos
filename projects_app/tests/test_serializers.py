from django.test import TestCase
from unittest.mock import Mock
from django.http import QueryDict
from . import recipes as project_recipes
from ..serializers import SprintSerializer, ProjectSerializer
from datetime import date

class SprintSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request = Mock()
        cls.request.query_params = QueryDict("")

    def test_validations_should_pass(self):
        data = {
            "name": "Sprint 1",
            "description": "Sprint 1 description",
            "start_date": "2023-01-01",
            "end_date": "2023-01-30",
        }

        serializer = SprintSerializer(data=data, context={"request": self.request})
        is_valid = serializer.is_valid(raise_exception=True)
        self.assertTrue(is_valid)

    def test_validations_should_fail_if_end_date_is_less_than_start_date(self):
        data = {
            "name": "Sprint 1",
            "description": "Sprint 1 description",
            "start_date": "2023-01-30",
            "end_date": "2023-01-01",
        }

        serializer = SprintSerializer(data=data, context={"request": self.request})
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertEqual(
            serializer.errors, {"non_field_errors": ["Start date must be before end date"]}
        )

    def test_validations_should_pass_if_end_date_is_equal_to_start_date(self):
        data = {
            "name": "Sprint 1",
            "description": "Sprint 1 description",
            "start_date": "2023-01-30",
            "end_date": "2023-01-30",
        }

        serializer = SprintSerializer(data=data, context={"request": self.request})
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)

    def test_validations_should_work_with_partial_update(self):
        sprint = project_recipes.sprint.make(
            start_date=date(2023, 1, 15), end_date=date(2023, 1, 30)
        )
        data = {
            "end_date": "2023-01-01",
        }

        serializer = SprintSerializer(
            sprint, data=data, context={"request": self.request}, partial=True
        )
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)        
        self.assertEqual(
            serializer.errors, {"non_field_errors": ["Start date must be before end date"]}
        )

    def test_get_tasks_count(self):
        sprint = project_recipes.sprint.make()
        project_recipes.task.make(sprint=sprint)
        project_recipes.task.make(sprint=sprint)
        serializer = SprintSerializer(sprint, context={"request": self.request})
        self.assertEqual(serializer.data["tasks_count"], 2)

class ProjectSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request = Mock()
        cls.request.query_params = QueryDict("")

    def test_get_tasks_count(self):
        project = project_recipes.project.make()
        project_recipes.task.make(project=project)
        project_recipes.task.make(project=project)
        serializer = ProjectSerializer(project, context={"request": self.request})
        self.assertEqual(serializer.data["tasks_count"], 2)

