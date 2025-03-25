from django.contrib import admin
from django.urls import path,include
from texnomart.views import  *
app_name = 'texnomart'
urlpatterns = [
    path('product-list/', ProductListOrCreateG.as_view(),name='product-list'),
    path('product-list/<int:pk>/', ProductDetailG.as_view(),name='product-detail'),

]
