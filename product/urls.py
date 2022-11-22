from django.urls import path
from users import views
from product import views

from .views import (SoftwareCreateView, SoftwareListView,
                    HardwareListView,SoftwareUpdateView,HardwareUpdateView,UnAssignedView,HardwareAssignView,HardwareDetailView)

urlpatterns = [
    path('software', SoftwareCreateView.as_view(), name="SoftwareCreate"),
    path('software_list', SoftwareListView.as_view(), name="SoftwareList"),
    path('software/update/<int:pk>', SoftwareUpdateView.as_view(), name="SoftwareUpdate"),
    
    
    path('hardware', views.HardwareCreateView, name="HardwareCreate"),
    path('hardware_list', HardwareListView.as_view(), name="HardwareList"),
    path('hardware/update/<int:pk>', HardwareUpdateView.as_view(), name="HardwareUpdate"),
    # path('hardware/detail/<int:pk>', HardwareDetailView.as_view(), name="HardwareDetail"),
    path('hardware/detail/<int:pk>', views.HardwareDetailView, name="HardwareDetail"),
    path('hardware/assign/<int:pk>', HardwareAssignView.as_view(), name="HardwareAssign"),
    # path('hardware/return/<int:pk>', HardwareReturnView.as_view(), name="HardwareReturn"),
    path('hardware/return/<int:pk>', views.HardwareReturn, name="HardwareReturn"),
    
    
    path('assignassets', views.AssignedView, name="AssignAsset"),
    path('unassignassets', UnAssignedView.as_view(), name="UnAssignAsset"),
    
    path('ajax/load-category', views.load_category, name='ajax_load_category'), # AJAX
    path('ajax/load-location', views.load_location, name='ajax_load_location'), # AJAX
    
    
]
