"""
URL configuration for insuresync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from setups.views import ProductCreateView, ProductListView, ProductUpdateView, VehicleMakeCreateView, VehicleMakeListView, VehicleMakeUpdateView, VehicleMakeDeleteView

urlpatterns = [
    path('product/create', ProductCreateView.as_view(), name='product-create'),
    path('product/list', ProductListView.as_view(), name='product-list'),
    path('update-product/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('make/create', VehicleMakeCreateView.as_view(), name='make-create'),
    path('make/list', VehicleMakeListView.as_view(), name='make-list'),
    path('update-vehiclemake/<int:pk>/', VehicleMakeUpdateView.as_view(), name='make-update'),
    path('delete-vehiclemake/<int:pk>/', VehicleMakeDeleteView.as_view(), name='make-delete')
]
