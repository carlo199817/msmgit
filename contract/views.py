from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import User, Contract, Product, Posm
from django.utils import timezone
from datetime import date, timedelta

from .serializers import ContractSerializer, ProductSerializer, PosmSerializer


class ContractListView(generics.ListCreateAPIView):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContractSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Contract.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)




class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()





class PosmListView(generics.ListCreateAPIView):
    serializer_class = PosmSerializer
    queryset = Posm.objects.all()
    permission_classes = (permissions.IsAuthenticated,)



class PosmDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PosmSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Posm.objects.all()



