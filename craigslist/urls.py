from django.contrib import admin
from django.urls import URLPattern, path, re_path
from django.urls import include
from craigslist.views.vehicles import VehiclesView

urlpatterns = [
    path('vehicles', VehiclesView.as_view())
]