from django.db import models
from django.utils import timezone

class CashMovementType(models.TextChoices):
    TRADE_PROCEED = 'trade_proceed', 'Trade Proceed'
    FEE = 'fee', 'Fee'
    DIVIDEND = 'dividend', 'Dividend'
    INTEREST = 'interest', 'Interest'
    DEPOSIT_WITHDRAWAL = 'deposit/withdrawal', 'Deposit/Withdrawal'


class PLType(models.TextChoices):
    DAY_1 = 'day_1', 'Day 1'
    MTM = 'mtm', 'Mark To Market'
    BROKERAGE = 'brokerage', 'Brokerage'


class Side(models.TextChoices):
    BUY = 'B', 'Buy'
    SELL = 'S', 'Sell'


class Holiday(models.Model):
    holiday_date = models.DateField()
    holiday_name = models.CharField(max_length=255)

    def __str__(self):
        return self.holiday_name
    

class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=3)
    
    constraints = [
        models.UniqueConstraint(fields=['currency_name', 'symbol'], name='unique_currency_symbol')
        ]    

    def __str__(self):
        return self.symbol
    
    
class Exchange(models.Model):
    exchange = models.CharField(max_length=255)

    def __str__(self):
        return self.exchange
    

class Instrument(models.Model):
    symbol = models.CharField(max_length=5)
    exchange_id = models.ForeignKey(Exchange, on_delete=models.PROTECT)
    currency_id = models.ForeignKey(Currency, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.symbol
    

class FilterCategory(models.Model):
    filter_category_code = models.CharField(max_length=255)
    filter_category = models.CharField(max_length=255)

    def __str__(self):
        return self.filter_category
    

class OrderingOption(models.Model):
    order_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class ViewOption(models.Model):
    view_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    

class SavedFilter(models.Model):
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_update = models.DateTimeField(default=timezone.now)
    filter = models.JSONField()  # Django 3.1+ has JSONField
    ordering = models.ForeignKey(OrderingOption, on_delete=models.PROTECT, blank=True, null=True)
    view = models.ForeignKey(ViewOption, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.description
    

class Trade(models.Model):
    trade_date = models.DateField()
    quantity = models.IntegerField()
    side = models.CharField(
        max_length=1,
        choices=Side.choices
    )
    price = models.DecimalField(max_digits=20, decimal_places=2)
    brokerage = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.PROTECT)
    brokerage_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.side} {self.quantity} \@ {self.price} on {self.trade_date}"
    

class HistoricalPosition(models.Model):
    report_date = models.DateField()
    quantity = models.IntegerField()
    side = models.CharField(
        max_length=1,
        choices=Side.choices
    )
    instrument = models.ForeignKey(Instrument, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.report_date} {self.side} {self.quantity}"
    

class HistoricalPL(models.Model):
    report_date = models.DateField()
    pl = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pl_type = models.CharField(
        max_length=255,
        choices=PLType.choices
    )
    instrument = models.ForeignKey(Instrument, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.report_date} {self.instrument} {self.pl_type} {self.pl}"
    

class FilterResult(models.Model):
    filter_id = models.ForeignKey(SavedFilter, on_delete=models.PROTECT)
    COB_date = models.DateField()
    run_date = models.DateTimeField(default=timezone.now)
    results = models.JSONField()


class FilterOption(models.Model):
    filter_category_id = models.ForeignKey(FilterCategory, on_delete=models.PROTECT)
    filter_option_code = models.CharField(max_length=255)
    filter_option = models.CharField(max_length=255)

    def __str__(self):
        return self.filter_option


class ClosePrice(models.Model):
    report_date = models.DateField()
    close_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.PROTECT)

    constraints = [
        models.UniqueConstraint(fields=['report_date', 'instrument'], name='unique_report_date_instrument')
        ]   

    def __str__(self):
        return f"{self.report_date} {self.instrument} {self.close_price}"