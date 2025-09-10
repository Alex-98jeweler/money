from rest_framework import serializers
from . import models


class TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Type
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Status
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.SubCategory
        fields = '__all__'
