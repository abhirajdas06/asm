from django.urls import path
from users import views
from product import views

from .views import (SoftwareCreateView, SoftwareListView,
                    HardwareCreateView, HardwareListView,SoftwareUpdateView,HardwareUpdateView,UnAssignedView,AssignedView,HardwareAssignView,HardwareDetailView)


urlpatterns = [
    path('software', SoftwareCreateView.as_view(), name="SoftwareCreate"),
    path('software_list', SoftwareListView.as_view(), name="SoftwareList"),
    path('software/update/<int:pk>', SoftwareUpdateView.as_view(), name="SoftwareUpdate"),
    
    
    path('hardware', HardwareCreateView.as_view(), name="HardwareCreate"),
    path('hardware_list', HardwareListView.as_view(), name="HardwareList"),
    path('hardware/update/<int:pk>', HardwareUpdateView.as_view(), name="HardwareUpdate"),
    path('hardware/detail/<int:pk>', HardwareDetailView.as_view(), name="HardwareDetail"),
    path('hardware/assign/<int:pk>', HardwareAssignView.as_view(), name="HardwareAssign"),
    # path('hardware/return/<int:pk>', HardwareReturnView.as_view(), name="HardwareReturn"),
    path('hardware/return/<int:pk>', views.HardwareReturn, name="HardwareReturn"),
    
    
    path('assignassets', AssignedView.as_view(), name="AssignAsset"),
    path('unassignassets', UnAssignedView.as_view(), name="UnAssignAsset"),
    
    
]
