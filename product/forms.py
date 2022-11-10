from django import forms
from .models import (Software, Hardware)
from master.models import SubCategory,Brand

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
        fields = ['name',	 'category','subcategory',	'barcode',	'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'warranty_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'tpm_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
            
            super().__init__(*args, **kwargs)
            self.fields['subcategory'].queryset = SubCategory.objects.none()
                    
            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name',		'category',	'subcategory',	'barcode',	'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'warranty_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'tpm_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
       
 
 
class HardwareAssignForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name',	'barcode',	'serial',	
                  	'status',	'location',	'assigned_to']
        widgets={
            "name": forms.TextInput(attrs={'readonly':True}),
            
            "barcode": forms.TextInput(attrs={'readonly':True}),
            "serial": forms.TextInput(attrs={'readonly':True}),
            "status": forms.TextInput(attrs={'readonly':True}),
            "location": forms.TextInput(attrs={'readonly':True}),
        }
   
class HardwareDetailForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name', 'category','subcategory',	'barcode',	'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            "name": forms.TextInput(attrs={'readonly':True}),
            'category': forms.TextInput(attrs={'readonly':True}),
            'subcategory': forms.TextInput(attrs={'readonly':True}),
            'vendor': forms.TextInput(attrs={'readonly':True}),
            'purchased_on': forms.TextInput(attrs={'readonly':True}),
            'warranty_expiry': forms.TextInput(attrs={'readonly':True}),
            'tpm_expiry': forms.TextInput(attrs={'readonly':True}),
            # 'assigned_to': forms.TextInput(attrs={'readonly':True}),
           
            "barcode": forms.TextInput(attrs={'readonly':True}),
            "serial": forms.TextInput(attrs={'readonly':True}),
            "status": forms.TextInput(attrs={'readonly':True}),
            "location": forms.TextInput(attrs={'readonly':True}),
        }        