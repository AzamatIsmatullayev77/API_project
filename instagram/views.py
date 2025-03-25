from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.models import Post


# Create your views here.
class PostListView(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        return Response({})