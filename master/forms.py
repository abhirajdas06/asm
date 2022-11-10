from django import forms
from .models import (Company, Branch, Employee_Location, Vendor, Asset_Location, Category, SubCategory, Brand, SoftwareType)
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# COMPANY MASTER FORM
class CompanyForm(forms.ModelForm):
    contact = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="IN"))
    
    class Meta:
        model = Company
        fields = ['company_name','address','contact','email','website']
        

# BRANCH MASTER FORM


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['company', 'branch_name','address']

# EMPLOYEE LOCATION MASTER FORM


class Employee_LocationForm(forms.ModelForm):
    class Meta:
        model = Employee_Location
        fields = ['branch', 'location']

# VENDOR FORM


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


#ASSET LOCATION FORM
class Asset_LocationForm(forms.ModelForm):
    class Meta:
        model = Asset_Location
        fields = ['branch', 'location']

#CATEGORY FORM
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

#SUBCATEGORY FORM
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name']

#BRAND FORM
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

#SOFTWARE TYPE FORM
class SoftwareTypeForm(forms.ModelForm):
    class Meta:
        model = SoftwareType
        fields = ['type']