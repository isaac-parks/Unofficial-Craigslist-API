from django.contrib import admin
from django.urls import URLPattern, path, re_path
from django.urls import include
import craigslist.views as views

urlpatterns = [
    path('vehicles', views.vehicles)
]