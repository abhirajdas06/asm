from django.urls import path
from users import views
from .views import (SoftwareCreateView, SoftwareListView,
                    HardwareCreateView, HardwareListView,SoftwareUpdateView,HardwareUpdateView)


urlpatterns = [
    path('software', SoftwareCreateView.as_view(), name="SoftwareCreate"),
    path('software_list', SoftwareListView.as_view(), name="SoftwareList"),
    path('software/update/<int:pk>', SoftwareUpdateView.as_view(), name="SoftwareUpdate"),
    
    
    path('hardware', HardwareCreateView.as_view(), name="HardwareCreate"),
    path('hardware_list', HardwareListView.as_view(), name="HardwareList"),
    path('hardware/update/<int:pk>', HardwareUpdateView.as_view(), name="HardwareUpdate"),
    
    
]
