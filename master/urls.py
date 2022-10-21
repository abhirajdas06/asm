from django.urls import path
from users import views
from .views import (

    CompanyCreateView,
    CompanyListView,
    CompanyUpdateView,
    BranchCreateView,
    BranchListView,
    EmployeeLocationCreateView,
    EmployeeLocationListView,
    VendorCreateView,
    VendorListView,
    AssetLocationCreateView,
    AssetLocationListView,
    CategoryCreateView,
    CategoryListView,
    SubCategoryCreateView,
    SubCategoryListView,
    BrandCreateView,
    BranchUpdateView,
    BrandListView,
    SoftwareTypeCreateView,
    SoftwareTypeListView
)


urlpatterns = [
    path('company', CompanyCreateView.as_view(), name="CompanyCreate"),
    path('company_list', CompanyListView.as_view(), name="CompanyList"),
    path('company/<int:pk>/update',CompanyUpdateView.as_view(), name="CompanyUpdate"),
    path('branch', BranchCreateView.as_view(), name="BranchCreate"),
    path('branch/<int:pk>/update',BranchUpdateView.as_view(), name="BranchUpdate"),
    path('branch_list', BranchListView.as_view(), name="BranchList"),
    path('employee_location', EmployeeLocationCreateView.as_view(),name="EmployeeLocationCreate"),
    path('employee_location_list', EmployeeLocationListView.as_view(), name="EmployeeLocationList"),
    path('vendor', VendorCreateView.as_view(), name="VendorCreate"), path('vendor_list', VendorListView.as_view(), name="VendorList"),
    path('asset_location', AssetLocationCreateView.as_view(), name="AssetLocationCreate"),
    path('asset_location_list', AssetLocationListView.as_view(), name="AssetLocationList"),
    path('category', CategoryCreateView.as_view(), name="CategoryCreate"),
    path('category_list', CategoryListView.as_view(), name="CategoryList"),
    path('subcategory', SubCategoryCreateView.as_view(), name="SubCategoryCreate"),
    path('subcategory_list', SubCategoryListView.as_view(), name="SubCategoryList"),
    path('brand', BrandCreateView.as_view(), name="BrandCreate"),
    path('brand_list', BrandListView.as_view(), name="BrandList"),
    path('software_type', SoftwareTypeCreateView.as_view(), name="SoftwareTypeCreate"),
    path('software_type_list', SoftwareTypeListView.as_view(), name="SoftwareTypeList"),
]
