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
        fields = ['name',	 'category','asset_type',	'barcode',	'serial',	'vendor','branch','cost',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'warranty_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'tpm_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
            
            super().__init__(*args, **kwargs)
            # filter(location_type='Asset Location')
            self.fields['location'].queryset = Location.objects.none()
            self.fields['category'].queryset = Category.objects.filter(asset_type='IT Assets')
            

                    
            if 'branch' in self.data:
                try:
                    
                    branch_id = int(self.data.get('branch'))
                    self.fields['location'].queryset = Location.objects.filter(branch_id=branch_id).order_by('location')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['location'].queryset = self.instance.category_set.order_by('location')
   
                    
    
class HardwareUpdateForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name',		'category',		'barcode',	'serial',	'vendor',
                  'purchased_on',	'warranty_expiry',	'tpm_expiry',	'status',	'location',	'assigned_to']
        widgets = {
            'purchased_on': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'warranty_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'tpm_expiry': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
            
            super().__init__(*args, **kwargs)
            self.fields['location'].queryset = Location.objects.filter(location_type='Asset Location')
 
 
class HardwareAssignForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [	'assigned_to','location']
        
        
   
    
    def __init__(self, *args, **kwargs):
            
            super().__init__(*args, **kwargs)
            self.fields['location'].queryset = Location.objects.none()
           
                    
            if 'assigned_to' in self.data:
                try:
                    location_id = int(self.data.get('assigned_to'))
                    self.fields['location'].queryset = Location.objects.filter(user__in=User.objects.filter(id=location_id))
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                pass
    #             # self.fields['location'].queryset = self.instance.assigned_to.order_by('location')
   
class HardwareDetailForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['name', 'category',	'barcode'	,'serial',	'vendor',
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
        
class HardwareReturnForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [	'location']