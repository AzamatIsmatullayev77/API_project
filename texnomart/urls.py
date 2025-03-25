from django.contrib import admin
from django.urls import path,include
from texnomart.views import  *
app_name = 'texnomart'
urlpatterns = [
    path('product-list/', ProductList.as_view(),name='product-list'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(),name='product-detail'),
]
