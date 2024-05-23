from django.test import TestCase
from . import recipes as project_recipes
from ..models import Sprint
from datetime import date

class SprintModelTestCase(TestCase):
    def test_start_date_must_be_before_end_date_should_pass(self):
        sprint = project_recipes.sprint.make(
            start_date=date(2023, 1, 1), end_date=date(2023, 1, 30)
        )
        self.assertIsNotNone(sprint)

    def test_start_date_must_be_before_end_date_should_fail(self):
        with self.assertRaises(Exception) as context:
            project_recipes.sprint.make(
                start_date=date(2023, 1, 30), end_date=date(2023, 1, 1)
            )
        self.assertIn("start_date_must_be_before_end_date", str(context.exception))