from django.shortcuts import render
from rest_framework import generics
from .serializers import CurrencySerializer
from .models import Currency

class CurrencyListCreate(generics.ListCreateAPIView):
    # queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def get_queryset(self):
        return Currency.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 