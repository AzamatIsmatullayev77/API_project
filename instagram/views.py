from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.models import Post
from instagram.serializers import PostModelSerializer


# Create your views here.
class PostListView(APIView):
    permission_classes = [AllowAny]


    def get(self, request, format=None):
        posts = Post.objects.all()
        serializers= PostModelSerializer(posts, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class PostDetailView(APIView):
    def get(self, request, pk, format=None):
        post = Post.objects.get(id=pk)
        serializers = PostModelSerializer(post)
        return Response(serializers.data)


class PostCreateView(APIView):
    def post(self,request):
        serializers = PostModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)