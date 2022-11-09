from rest_framework import serializers
from .models import User, ProductInventory, PosmInventory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class ProductInventorySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = ProductInventory
        fields = ['id','author', 'product','product_no','sku','quantity','price','date_posted','datenow']



class PosmInventorySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = PosmInventory
        fields = ['id','author', 'posm','quantity','price','sku','posm_no','date_posted','datenow']

