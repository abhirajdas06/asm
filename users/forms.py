from django import forms
from .models import (User, Company, Branch, Employee_Location)
from django.contrib.auth.forms import UserCreationForm
from users.models import Employee_Location

#USER CREATION FORM
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'employee_code', 'email', 'password1',
                  'password2', 'branch', 'user_type', 'office_contact', 'contact', 'location', 'active']
        
        
    def __init__(self, *args, **kwargs):
            
            super().__init__(*args, **kwargs)
            self.fields['location'].queryset = Employee_Location.objects.none()
                    
            if 'branch' in self.data:
                try:
                    branch_id = int(self.data.get('branch'))
                    self.fields['location'].queryset = Employee_Location.objects.filter(branch_id=branch_id).order_by('location')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['location'].queryset = self.instance.category.subcategory_set.order_by('location')

#USER UPDATE FORM
class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'employee_code', 'email', 'branch',
                  'user_type', 'office_contact', 'contact', 'location', 'active']


#COMPANY MASTER FORM
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'address', 'contact']

#BRANCH MASTER FORM
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['company', 'branch_location']

#EMPLOYEE LOCATION MASTER FORM
class Employee_LocationForm(forms.ModelForm):
    class Meta:
        model = Employee_Location
        fields = ['branch', 'location']