from rest_framework import serializers
from .models import Contract, User, Product, Posm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(max_length=200)
    class Meta:
        model = Product
        fields = ['id','product_id','name']

class PosmSerializer(serializers.ModelSerializer):
     posm_id = serializers.CharField(max_length=200)
     class Meta:
                model = Posm
                fields = ['id', 'posm_id', 'name']

class ContractSerializer(serializers.ModelSerializer):
    posm = PosmSerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(many=False)
    image = serializers.ImageField(use_url=True, required=False)
    class Meta:
        model = Contract
        fields = ['id','author', 'firstname', 'middlename', 'lastname',
                  'extension','birthdate','mobilenumber',
                  'email','agree','datenow','timenow','latitude','longitude','product','posm','image','store','date_posted','gender']

