from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

class HolidayListCreate(generics.ListCreateAPIView):
    # queryset = Currency.objects.all()
    serializer_class = serializers.HolidaySerializer

    def get_queryset(self):
        return models.Holiday.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 
    
class CurrencyListCreate(generics.ListCreateAPIView):
    # queryset = Currency.objects.all()
    serializer_class = serializers.CurrencySerializer

    def get_queryset(self):
        return models.Currency.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class ExchangeListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ExchangeSerializer

    def get_queryset(self):
        return models.Exchange.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class InstrumentListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.InstrumentSerializer

    def get_queryset(self):
        return models.Instrument.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class FilterCategoryListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.FilterCategorySerializer

    def get_queryset(self):
        return models.FilterCategory.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return  

class OrderingOptionListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.OrderingOptionSerializer

    def get_queryset(self):
        return models.OrderingOption.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class ViewOptionListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ViewOptionSerializer

    def get_queryset(self):
        return models.ViewOption.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class SavedFilterListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.SavedFilterSerializer

    def get_queryset(self):
        return models.SavedFilter.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class TradeListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.TradeSerializer

    def get_queryset(self):
        return models.Trade.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class HistoricalPositionListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.HistoricalPositionSerializer

    def get_queryset(self):
        return models.HistoricalPosition.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class HistoricalPLListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.HistoricalPLSerializer

    def get_queryset(self):
        return models.HistoricalPL.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class FilterResultListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.FilterResultSerializer

    def get_queryset(self):
        return models.FilterResult.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class FilterOptionListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.FilterOptionSerializer

    def get_queryset(self):
        return models.FilterOption.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 

class ClosePriceListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ClosePriceSerializer

    def get_queryset(self):
        return models.ClosePrice.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return 