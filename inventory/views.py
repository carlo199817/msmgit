from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import User, ProductInventory, PosmInventory
from django.utils import timezone
from datetime import date, timedelta

from .serializers import ProductInventorySerializer, PosmInventorySerializer


class ProductInventoryListView(generics.ListCreateAPIView):
    serializer_class = ProductInventorySerializer
    queryset = ProductInventory.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class ProductInventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductInventorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductInventory.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

class PosmInventoryListView(generics.ListCreateAPIView):
    serializer_class = PosmInventorySerializer
    queryset = PosmInventory.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PosmInventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PosmInventorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PosmInventory.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)