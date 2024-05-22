from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    """It is a company which may have multiple users related"""

    name = models.CharField(max_length=128)
    main_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class User(AbstractUser):
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="users", null=True, blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def is_customer(self):
        return self.customer is not None
