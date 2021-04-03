from rest_framework import viewsets
from storage.models import Category, Model3d
from storage.serializers import CategorySerializer, Model3dSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class Model3dViewSet(viewsets.ModelViewSet):
    serializer_class = Model3dSerializer
    queryset = Model3d.objects.all()