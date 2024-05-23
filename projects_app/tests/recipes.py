import datetime 
from model_bakery import recipe
from faker import Faker
from auth_app.tests import recipes as auth_recipes
fake = Faker("pt_BR")

from ..models import (
    Project,
    Sprint,
    Task,
)

sprint = recipe.Recipe(
    Sprint,
    name = fake.name,
    description = fake.text,
    start_date = datetime.date.today(),
    end_date = datetime.date.today() + datetime.timedelta(days=7),
)

project = recipe.Recipe(
    Project,
    name = fake.name,
    description = fake.text,
    customer = recipe.foreign_key(auth_recipes.customer),
)

task = recipe.Recipe(
    Task,
    name = fake.name,
    description = fake.text,
    project = recipe.foreign_key(project),
    sprint = recipe.foreign_key(sprint),
    reporter = recipe.foreign_key(auth_recipes.user),
    assignee = recipe.foreign_key(auth_recipes.user),
)