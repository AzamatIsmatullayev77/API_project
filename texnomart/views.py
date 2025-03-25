from rest_framework.generics import GenericAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Max, Min, Count, Avg
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from texnomart.models import Product, Images
from texnomart.serializers import ProductModelSerializer, ImageSerializer


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


# class ProductListOrCreate(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializers = ProductModelSerializer(products, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializers = ProductModelSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductDetail(APIView):
#     def get(self, request, pk, format=None):
#         try:
#             product = Product.objects.get(id=pk)
#             serializers = ProductModelSerializer(product)
#             return Response(serializers.data, status=status.HTTP_200_OK)
#         except Product.DoesNotExist:
#             return Response({'error':'product does not exist'},status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk=None):
#         product = Product.objects.get(pk=pk)
#         if product:
#             product.delete()
#             data = {"massage": "deleted"}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
#         data = {"massage": "product not found"}
#         return Response(data, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, pk=None):
#         product = Product.objects.get(pk=pk)
#         serializers = ProductModelSerializer(request.data,instance=product)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListOrCreateG(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailG(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ImageListOrCreateG(ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImageDetailG(RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
