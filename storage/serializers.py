from rest_framework import serializers
from .models import Category, Model3d


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class Model3dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3d
        fields = ('id', 'name', 'category', 'image', 'describe', 'price', 'object')