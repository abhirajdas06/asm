from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from .models import (Company, Branch, Employee_Location, Vendor,
                     Asset_Location, Category, SubCategory, Brand, SoftwareType)
from .forms import (CompanyForm, BranchForm, Employee_LocationForm, VendorForm,
                    Asset_LocationForm, CategoryForm, SubCategoryForm, BrandForm, SoftwareTypeForm)


# COMPANY MASTER CREATE
@method_decorator(login_required, name='dispatch')
class CompanyCreateView(generic.CreateView):
    template_name = 'master/company/company_create.html'
    form_class = CompanyForm

    def get_success_url(self):
        messages.success(self.request, 'Company Created Sucessfully')
        return reverse("CompanyList")


# COMPANY MASTER LIST
@method_decorator(login_required, name='dispatch')
class CompanyListView(generic.ListView):
    template_name = "master/company/company_list.html"
    queryset = Company.objects.all()
    context_object_name = "company"


# COMPANY BRANCH CREATE
@method_decorator(login_required, name='dispatch')
class BranchCreateView(generic.CreateView):
    template_name = 'master/branch/branch_create.html'
    form_class = BranchForm

    def get_success_url(self):
        messages.success(self.request, 'Branch Created Sucessfully')
        return reverse("BranchList")


# COMPANY BRANCH LIST
@method_decorator(login_required, name='dispatch')
class BranchListView(generic.ListView):
    template_name = "master/branch/branch_list.html"
    queryset = Branch.objects.all()
    context_object_name = "branch"


# COMPANY EMPLOYEE LOCATION CREATE
@method_decorator(login_required, name='dispatch')
class EmployeeLocationCreateView(generic.CreateView):
    template_name = 'master/location/employee_location_create.html'
    form_class = Employee_LocationForm

    def get_success_url(self):
        messages.success(self.request, 'Branch Created Sucessfully')
        return reverse("BranchList")


# COMPANY EMPLOYEE LOCATION LIST
@method_decorator(login_required, name='dispatch')
class EmployeeLocationListView(generic.ListView):
    template_name = "master/location/employee_location_list.html"
    queryset = Employee_Location.objects.all()
    context_object_name = "e_location"


# VENDOR CREATE
@method_decorator(login_required, name='dispatch')
class VendorCreateView(generic.CreateView):
    template_name = 'master/vendor/vendor_create.html'
    form_class = VendorForm

    def get_success_url(self):
        messages.success(self.request, 'Vendor Created Sucessfully')
        return reverse("VendorList")


# VENDOR LIST
@method_decorator(login_required, name='dispatch')
class VendorListView(generic.ListView):
    template_name = "master/vendor/vendor_list.html"
    queryset = Vendor.objects.all()
    context_object_name = "vendor"


# COMPANY ASSET LOCATION CREATE
@method_decorator(login_required, name='dispatch')
class AssetLocationCreateView(generic.CreateView):
    template_name = 'master/location/asset_location_create.html'
    form_class = Asset_LocationForm

    def get_success_url(self):
        messages.success(self.request, 'Branch Created Sucessfully')
        return reverse("EmployeeLocationList")


# COMPANY ASSET LOCATION LIST
@method_decorator(login_required, name='dispatch')
class AssetLocationListView(generic.ListView):
    template_name = "master/location/asset_location_list.html"
    queryset = Asset_Location.objects.all()
    context_object_name = "a_location"


# PRODUCT CATEGORY CREATE
@method_decorator(login_required, name='dispatch')
class CategoryCreateView(generic.CreateView):
    template_name = 'master/category/category_create.html'
    form_class = CategoryForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("CategoryList")


# PRODUCT CATEGORY LIST
@method_decorator(login_required, name='dispatch')
class CategoryListView(generic.ListView):
    template_name = "master/category/category_list.html"
    queryset = Category.objects.all()
    context_object_name = "category"


# PRODUCT SUBCATEGORY CREATE
@method_decorator(login_required, name='dispatch')
class SubCategoryCreateView(generic.CreateView):
    template_name = 'master/category/sub_category_create.html'
    form_class = SubCategoryForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("SubCategoryList")


# PRODUCT SUBCATEGORY LIST
@method_decorator(login_required, name='dispatch')
class SubCategoryListView(generic.ListView):
    template_name = "master/category/sub_category_list.html"
    queryset = SubCategory.objects.all()
    context_object_name = "subcategory"


# PRODUCT BRAND CREATE
@method_decorator(login_required, name='dispatch')
class BrandCreateView(generic.CreateView):
    template_name = 'master/brand/brand_create.html'
    form_class = BrandForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("BrandList")


# PRODUCT BRAND LIST
@method_decorator(login_required, name='dispatch')
class BrandListView(generic.ListView):
    template_name = "master/brand/brand_list.html"
    queryset = Brand.objects.all()
    context_object_name = "brand"


# SOFTWARE TYPE CREATE
@method_decorator(login_required, name='dispatch')
class SoftwareTypeCreateView(generic.CreateView):
    template_name = 'master/type/s_type_create.html'
    form_class = SoftwareTypeForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("SoftwareTypeList")


# SOFTWARE TYPE LIST
@method_decorator(login_required, name='dispatch')
class SoftwareTypeListView(generic.ListView):
    template_name = "master/type/s_type_list.html"
    queryset = SoftwareType.objects.all()
    context_object_name = "s_type"
