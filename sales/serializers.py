from rest_framework import serializers
from .models import User, Sales, SalesTotal
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class SalesSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Sales
        fields = ['id','author', 'product','quantity','price','datenow','timenow']



class SalesTotalSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    datenow = serializers.CharField(validators=[
        UniqueValidator(
            queryset=SalesTotal.objects.all(),
            message="row already exist",
        )]
    )
    class Meta:
        model = SalesTotal
        fields = ['id','author', 'total','datenow','date_posted','timenow']

