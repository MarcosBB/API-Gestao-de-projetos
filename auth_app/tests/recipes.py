from django.utils import timezone
from model_bakery import recipe
from faker import Faker
from ..models import User, Customer

fake = Faker("pt_BR")

customer = recipe.Recipe(
    Customer,
    name = fake.company,
    main_email = fake.email,
)


user = recipe.Recipe(
    User,
    first_name = fake.first_name,
    last_name = fake.last_name,
    email = fake.email,
    username = fake.user_name,
    is_active = True,
)

customer_user = user.extend(
    customer = recipe.foreign_key(customer),
)

admin_user = user.extend(
    is_staff = True,
    is_superuser = True,
)
