from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from .models import (Software, Hardware)
from .forms import (SoftwareForm, HardwareForm)


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


# HARDWARE PRODUCT CREATE
@method_decorator(login_required, name='dispatch')
class HardwareCreateView(generic.CreateView):
    template_name = 'product/hardware/hardware_create.html'
    form_class = HardwareForm

    def get_success_url(self):
        messages.success(self.request, 'Hardware Created Sucessfully')
        return reverse("HardwareList")


# HARDWARE PRODUCT LIST
@method_decorator(login_required, name='dispatch')
class HardwareListView(generic.ListView):
    template_name = "product/hardware/hardware_list.html"
    queryset = Hardware.objects.all()
    context_object_name = "hardware"
