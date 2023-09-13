from rest_framework import serializers
from onlineshop.models import Categories, Products



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
        

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'