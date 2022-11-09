from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import StoreSerializer
from .models import Store, User
from rest_framework import status

class StoreAllListView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        try:
            author_search = self.request.data.get('author')
            u = User.objects.get(username=author_search)
            query_set = Store.objects.filter(author=u)
            serializers = StoreSerializer(query_set,many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'invalid username or email',

            }, status=status.HTTP_400_BAD_REQUEST)


class StoreListView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        u = User.objects.get(username=author)
        return Store.objects.filter(author=u)




class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Store.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


