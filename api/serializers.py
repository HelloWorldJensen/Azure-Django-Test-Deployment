from rest_framework import serializers
from . import models

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holiday
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = '__all__'

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exchange
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instrument
        fields = '__all__'

class FilterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilterCategory
        fields = '__all__'

class OrderingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderingOption
        fields = '__all__'

class ViewOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ViewOption
        fields = '__all__'

class SavedFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavedFilter
        fields = '__all__'

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trade
        fields = '__all__'

class HistoricalPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoricalPosition
        fields = '__all__'

class HistoricalPLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoricalPL
        fields = '__all__'

class FilterResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilterResult
        fields = '__all__'

class FilterOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilterOption
        fields = '__all__'

class ClosePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClosePrice
        fields = '__all__'