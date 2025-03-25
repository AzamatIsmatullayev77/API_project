from rest_framework import serializers
from texnomart.models import Product,Images

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        exclude = ()

class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'