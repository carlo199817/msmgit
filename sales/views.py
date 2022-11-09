from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import User, Sales, SalesTotal
from django.utils import timezone
from datetime import datetime, timedelta
from backports.zoneinfo import ZoneInfo

from .serializers import SalesSerializer, SalesTotalSerializer


class SalesListView(generics.ListCreateAPIView):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        u = User.objects.get(username=author)
        time = datetime.now(ZoneInfo('Asia/Manila'))
        get_time = time.strftime("%-I%p")
        get_today = time.strftime("%Y-%m-%d")
        return Sales.objects.filter(author=u,datenow=get_today)

class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SalesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sales.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class SalesTotalListView(generics.ListCreateAPIView):
    serializer_class = SalesTotalSerializer
    queryset = SalesTotal.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        u = User.objects.get(username=author)
        time = datetime.now(ZoneInfo('Asia/Manila'))
        get_time = time.strftime("%-I%p")
        get_today = time.strftime("%Y-%m-%d")
        return SalesTotal.objects.filter(author=u)


class SalesTotalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SalesTotalSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SalesTotal.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
