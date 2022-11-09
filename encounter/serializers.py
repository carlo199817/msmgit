from rest_framework import serializers
from .models import Encounter, User, CheckContract


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class EncounterSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Encounter
        fields = ['id', 'checkmotor', 'date_posted', 'author', 'latitude','longitude','datenow','timenow']


class CheckContractSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = CheckContract
        fields = ['id', 'checkcontract', 'date_posted', 'author', 'latitude','longitude','datenow','timenow']

