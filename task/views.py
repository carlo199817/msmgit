from django.http import JsonResponse
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import AllowAny

from authentication.models import User
from task.models import Task, Gps
from task.serializers import TaskSerializer, GpsSerializer


class TaskViews(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    def get_queryset(self):
        email = self.request.user.email
        return Task.objects.filter(email=email)


class TaskAll(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class GpsViews(generics.ListCreateAPIView):
    serializer_class = GpsSerializer
    queryset = Gps.objects.all()
    permission_classes = (AllowAny,)

class GpsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GpsSerializer
    queryset = Gps.objects.all()
