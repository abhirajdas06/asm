from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from .models import (Software, Hardware)
from users.models import User
from master.models import SubCategory,Employee_Location
from .forms import (SoftwareForm, HardwareForm,HardwareDetailForm, HardwareAssignForm, HardwareCreateForm)


# SOFTWARE PRODUCT CREATE
@method_decorator(login_required, name='dispatch')
class SoftwareCreateView(generic.CreateView):
    template_name = 'product/software/software_create.html'
    form_class = SoftwareForm

    def get_success_url(self):
        messages.success(self.request, 'Software Created Sucessfully')
        return reverse("SoftwareList")


# SOFTWARE PRODUCT LIST
@method_decorator(login_required, name='dispatch')
class SoftwareListView(generic.ListView):
    template_name = "product/software/software_list.html"
    queryset = Software.objects.all()
    context_object_name = "software"
    
# SOFTWARE PRODUCT Update
@method_decorator(login_required, name='dispatch')
class SoftwareUpdateView(generic.UpdateView):
    template_name = "product/software/software_update.html"
    form_class=SoftwareForm
    queryset = Software.objects.all()
    context_object_name = "software"
    
    def get_success_url(self):
        return reverse("SoftwareList")



# HARDWARE PRODUCT CREATE
@method_decorator(login_required, name='dispatch')
class HardwareCreateView(generic.CreateView):
    template_name = 'product/hardware/hardware_create.html'
    form_class = HardwareCreateForm

    def get_success_url(self):
        messages.success(self.request, 'Hardware Created Sucessfully')
        return reverse("HardwareList")


# HARDWARE PRODUCT LIST
@method_decorator(login_required, name='dispatch')
class HardwareListView(generic.ListView):
    template_name = "product/hardware/hardware_list.html"
    queryset = Hardware.objects.all()

    context_object_name = "hardware"
    
    # HARDWARE PRODUCT UPDATE
@method_decorator(login_required, name='dispatch')
class HardwareUpdateView(generic.UpdateView):
    template_name = "product/hardware/hardware_update.html"
    form_class=HardwareForm
    queryset = Hardware.objects.all()
    context_object_name = "hardware"
    
    def get_success_url(self):
        return reverse("HardwareList")
    
    
@method_decorator(login_required, name='dispatch') 
class UnAssignedView(generic.ListView):
    template_name = "product/hardware/hardware_unassigned_list.html"
    # queryset = Product.objects.raw('Select * From product_product Where "assign_to_id" IS NULL')
    queryset = Hardware.objects.filter(assigned_to__id = None)
    context_object_name = "hardware"

@method_decorator(login_required, name='dispatch')    
class AssignedView(generic.ListView):
    template_name = "product/hardware/hardware_assigned_list.html"
    # queryset = Product.objects.raw('Select * From product_product Where NOT (assign_to_id=None)
    queryset = Hardware.objects.exclude(assigned_to__id = None)
    context_object_name = "hardware"

# @login_required
# def AssignedView(request):
#     pkid= Hardware.objects.exclude(assigned_to__id = None)
#     print(pkid)
#     # soft= User.objects.filter(location=pkid)
#     soft= Employee_Location.objects.select_related(pkid)
#     print(soft)
#     # form = HardwareDetailForm(instance=pkid)  
#     context ={
       
#         "hardware":pkid,
#         "software":soft,
        
#     }
#     return render(request,'product/hardware/hardware_assigned_list.html',context)
    
    
       # HARDWARE PRODUCT Assign
@method_decorator(login_required, name='dispatch')
class HardwareAssignView(generic.UpdateView):
    template_name = "product/hardware/hardware_assign.html"
    form_class=HardwareAssignForm
    queryset = Hardware.objects.all()
    context_object_name = "hardware"
    
    def get_success_url(self):
        return reverse("AssignAsset")

# HARDWARE PRODUCT Return in Stock
@login_required
def HardwareReturn(request,pk):
    
#     queryset = Hardware.objects.raw( Hardware
# SET assigned_to = None
# WHERE id=pk;)

    Hardware.objects.filter(id=pk).update(assigned_to=None)
    
    # q = Hardware.objects.get(id=pk)
    # q.assigned_to = None
    # q.save()
    return redirect ("UnAssignAsset")

# HARDWARE PRODUCT Detailview
# class HardwareDetailView(generic.DetailView):
#     model = Hardware
  
#     template_name= "product/hardware/hardware_detail.html"
    
    
@login_required
def HardwareDetailView(request,pk):
    pkid= Hardware.objects.get(id=pk)
    soft= Software.objects.filter(installed_on=pkid)
    form = HardwareDetailForm(instance=pkid)  
    context ={
        "form": form,
        "hardware":pkid,
        "software":soft,
        
    }
    return render(request,'product/hardware/hardware_detail.html',context)

@login_required
def load_category(request):
    category_id = request.GET.get('category_id')
    subcategory = SubCategory.objects.filter(category_id=category_id)
    return render(request, 'product/hardware/subcategory_dropdown_list.html', {'subcategory': subcategory})


    
    
    
