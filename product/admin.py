from django.contrib import admin
from .models import (Software,Hardware)

# Register your models here.
admin.site.register((Software,Hardware))