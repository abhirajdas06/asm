# import
from django.db import models
from django.contrib.auth.models import AbstractUser
from master.models import (Company, Branch, Employee_Location)


# USER MODEL


class User(AbstractUser):
    employee_code = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    contact = models.IntegerField(null=True)
    office_contact = models.IntegerField(null=True)
    user_type = models.CharField(max_length=30, choices=(
        ('admin', 'admin'), ('user', 'user')), null=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, null=True)
    location = models.ForeignKey(
        Employee_Location, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(("active"), default=True,)
