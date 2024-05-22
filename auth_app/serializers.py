from rest_framework import serializers
from .models import User, Customer
from rest_flex_fields import FlexFieldsModelSerializer


class CustomerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "main_email"]


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "customer"]
        expandable_fields = {"customer": (CustomerSerializer)}
