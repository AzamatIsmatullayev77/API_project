from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Max, Min, Count, Avg
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from texnomart.models import Product
from texnomart.serializers import ProductModelSerializer

# Create your views here.

# class PostList(APIView):
#     permission_classes = [AllowAny]
#
#     # authentication_classes = []
#     def get(self, request, format=None):
#         data={
#             'message': 'Hello World!',
#             'success': True,
#             'status_code': status.HTTP_200_OK,
#         }
#         return Response(data)

# @api_view(['GET'])
# def post_list(request):
#     data = {
#         'data': {
#             'message': 'Hello World!',
#             'success': True,
#             'status_code': status.HTTP_200_OK,
#         }
#     }
#     return Response(data)


# class PostList(APIView):
#     permission_classes = [AllowAny]
#
#     # authentication_classes = []
#     def get(self, request, format=None):
#         posts=Product.objects.all()
#         data=[]
#         for post in posts:
#             data.append({
#                 'id':post.id,
#                 'title':post.title,
#                 'price':post.price,
#                 'description':post.description,
#
#
#             })
#         return Response(data)


class ProductList(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        products = Product.objects.all()
        serializers=ProductModelSerializer(products, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get(self, request, pk,format=None):
        product = Product.objects.get(id=pk)
        serializers=ProductModelSerializer(product)
        return Response(serializers.data, status=status.HTTP_200_OK)