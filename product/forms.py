from django import forms
from .models import (Software, Hardware)
from master.models import Category,Brand,Location
from users.models import User

# COMPANY MASTER FORM
class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'softwaretype', 'purchased_on','installed_on', 'expiry']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class HardwareCreateForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name',	 'category','asset_type',	'barcode',	'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'warranty_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'tpm_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
        
    # def __init__(self, *args, **kwargs):
            
    #         super().__init__(*args, **kwargs)
    #         self.fields['category'].queryset = Category.objects.none()
                    
    #         if 'category' in self.data:
    #             try:
    #                 category_id = int(self.data.get('category'))
    #                 self.fields['category'].queryset = Category.objects.filter(category_id=category_id).order_by('name')
    #             except (ValueError, TypeError):
    #                 pass  # invalid input from the client; ignore and fallback to empty City queryset
    #         elif self.instance.pk:
    #             self.fields['subcategory'].queryset = self.instance.category_set.order_by('name')

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name',		'category',		'barcode',	'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'warranty_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'tpm_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
       
 
 
class HardwareAssignForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [	'assigned_to']
        
        
    # def __init__(self, *args, **kwargs):
            
    #         super().__init__(*args, **kwargs)
    #         self.fields['location'].queryset = Location.objects.all()
        # widgets={
        #     "name": forms.TextInput(attrs={'readonly':True}),
            
        #     "barcode": forms.TextInput(attrs={'readonly':True}),
        #     "serial": forms.TextInput(attrs={'readonly':True}),
        #     "status": forms.TextInput(attrs={'readonly':True}),
        #     "location": forms.TextInput(attrs={'readonly':True}),
       # }
    # def __init__(self, *args, **kwargs):
            
    #         super().__init__(*args, **kwargs)
    #         self.fields['location'].queryset = Employee_Location.objects.all()
           
                    
    #         if 'assigned_to' in self.data:
    #             try:
    #                 location_id = int(self.data.get('assigned_to'))
    #                 self.fields['location'].queryset = User.objects.filter(location=location_id).order_by('location')
    #             except (ValueError, TypeError):
    #                 pass  # invalid input from the client; ignore and fallback to empty City queryset
    #         elif self.instance.pk:
    #             pass
    #             # self.fields['location'].queryset = self.instance.assigned_to.order_by('location')
   
class HardwareDetailForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name', 'category',	'barcode','asset_type'	,'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        # widgets = {
        #     "name": forms.TextInput(attrs={'readonly':True}),
        #     'category': forms.TextInput(attrs={'readonly':True}),
            
        #     'vendor': forms.TextInput(attrs={'readonly':True}),
        #     'purchased_on': forms.TextInput(attrs={'readonly':True}),
        #     'warranty_expiry': forms.TextInput(attrs={'readonly':True}),
        #     'tpm_expiry': forms.TextInput(attrs={'readonly':True}),
        #     'assigned_to': forms.TextInput(attrs={'readonly':True}),
        #     "barcode": forms.TextInput(attrs={'readonly':True}),
        #     "serial": forms.TextInput(attrs={'readonly':True}),
        #     "status": forms.TextInput(attrs={'readonly':True}),
        #     "location": forms.TextInput(attrs={'readonly':True}),
        # }        