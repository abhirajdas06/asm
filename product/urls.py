from django.urls import path
from users import views
from .views import (SoftwareCreateView, SoftwareListView,
                    HardwareCreateView, HardwareListView)


urlpatterns = [
    path('software', SoftwareCreateView.as_view(), name="SoftwareCreate"),
    path('software_list', SoftwareListView.as_view(), name="SoftwareList"),
    path('hardware', HardwareCreateView.as_view(), name="HardwareCreate"),
    path('hardware_list', HardwareListView.as_view(), name="HardwareList"),
]
