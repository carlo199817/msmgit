from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import User,  Store, SProduct, SPosm
from django.utils import timezone
from datetime import datetime, timedelta
from backports.zoneinfo import ZoneInfo

from .serializers import  StoreSerializer, SProductSerializer, SPosmSerializer


class  IStoreListView(generics.ListCreateAPIView):
    serializer_class =  StoreSerializer
    queryset =  Store.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        u = User.objects.get(username=author)
        time = datetime.now(ZoneInfo('Asia/Manila'))
        get_time = time.strftime("%-I%p")
        get_today = time.strftime("%Y-%m-%d")
        return Store.objects.filter(author=u,datenow=get_today)

class  IStoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  StoreSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset =  Store.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class SProductListView(generics.ListCreateAPIView):
    serializer_class = SProductSerializer
    queryset = SProduct.objects.all()
    permission_classes = (permissions.IsAuthenticated,)




class SProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SProduct.objects.all()





class SPosmListView(generics.ListCreateAPIView):
    serializer_class = SPosmSerializer
    queryset = SPosm.objects.all()
    permission_classes = (permissions.IsAuthenticated,)



class SPosmDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SPosmSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SPosm.objects.all()



