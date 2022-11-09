
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Task,Gps





class GpsSerializer(serializers.ModelSerializer):
    gps_id = serializers.CharField(max_length=200)
    class Meta:
        model = Gps
        fields = ['id','gps_id','longitude','latitude']




class TaskSerializer(serializers.ModelSerializer):
    gps = GpsSerializer(many=True, read_only=True)
    email = serializers.CharField(validators=[
        UniqueValidator(
            queryset=Task.objects.all(),
            message="Email is already exist",
        )]
    )
    class Meta:
        model = Task
        fields = ['id', 'email','place','description','gps']

        def create(self, validated_data):
            tracks_data = validated_data.pop('gps')
            task = Task.objects.create(**validated_data)
            for track_data in tracks_data:
                Gps.objects.create(task=task, **track_data)
            return task