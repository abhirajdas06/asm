from django.contrib import admin
from .models import (Company, Branch, Employee_Location, Vendor, Asset_Location, Category, SubCategory, Brand, SoftwareType)

# Register your models here.
admin.site.register((Company, Branch, Employee_Location, Vendor, Asset_Location, Category, SubCategory, Brand, SoftwareType))