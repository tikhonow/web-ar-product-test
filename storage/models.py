from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Model3d(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    describe = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    object = models.FileField(null=False)

    def __str__(self):
        return self.name


admin.site.register(Model3d)
admin.site.register(Category)