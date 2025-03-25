from rest_framework import serializers
from texnomart.models import Product,Images
from texnomart.views import Comment


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        exclude = ()


class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)
    likes = serializers.SerializerMethodField()
    def get_likes(self, instance):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        if user not in instance.likes.all():
            return False
        return True
    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'