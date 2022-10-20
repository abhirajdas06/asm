import email
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# COMPANY


class Company(models.Model):
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    contact = models.IntegerField()

    def __str__(self):
        return self.company_name

# BRANCH


class Branch(models.Model):
    company = models.ForeignKey("Company", on_delete=models.PROTECT)
    branch_location = models.CharField(max_length=20)

    def __str__(self):
        return self.branch_location


# USER LOCATION


class Employee_Location(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

# VENDOR


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    vendor_number = models.CharField(max_length=50)
    vendor_contact = models.IntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name

# ASSET LOCATION


class Asset_Location(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

# CATEGORY


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# SUBCATEGORY


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# BRAND


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# SOFTWARE TYPE


class SoftwareType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type