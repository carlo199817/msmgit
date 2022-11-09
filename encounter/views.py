from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import EncounterSerializer, CheckContractSerializer
from .models import Encounter, User, CheckContract
from backports.zoneinfo import ZoneInfo
from datetime import datetime, timedelta

class EncounterListView(generics.ListCreateAPIView):
    serializer_class = EncounterSerializer
    queryset = Encounter.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        u = User.objects.get(username=author)
        time = datetime.now(ZoneInfo('Asia/Manila'))
        get_time = time.strftime("%-I%p")
        get_today = time.strftime("%Y-%m-%d")
        return Encounter.objects.filter(author=u,datenow=get_today)





class EncounterDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EncounterSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Encounter.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

class CheckContractListView(generics.ListCreateAPIView):
    serializer_class = CheckContractSerializer
    queryset = CheckContract.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        u = User.objects.get(username=author)
        time = datetime.now(ZoneInfo('Asia/Manila'))
        get_time = time.strftime("%-I%p")
        get_today = time.strftime("%Y-%m-%d")
        return CheckContract.objects.filter(author=u,datenow=get_today)








class CheckContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CheckContractSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CheckContract.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


