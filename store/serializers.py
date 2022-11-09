from rest_framework import serializers
from .models import Store, User,SProduct, SPosm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class SProductSerializer(serializers.ModelSerializer):
    sproduct_id = serializers.CharField(max_length=200)
    class Meta:
        model = SProduct
        fields = ['id','sproduct_id','name','quantity','price']

class SPosmSerializer(serializers.ModelSerializer):
     sposm_id = serializers.CharField(max_length=200)
     class Meta:
                model = SPosm
                fields = ['id', 'sposm_id', 'name','quantity','price']

class  StoreSerializer(serializers.ModelSerializer):
    sposm = SPosmSerializer(many=True, read_only=True)
    sproduct = SProductSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(many=False)
    image = serializers.ImageField(use_url=True, required=False)
    class Meta:
        model =  Store
        fields = ['id','author','datenow','timenow','latitude','longitude','sproduct','sposm','image','store','date_posted']

