from django.db import models

class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=3)
    
    constraints = [
        models.UniqueConstraint(fields=['currency_name', 'symbol'], name='unique_currency_symbol')
        ]    

    def __str__(self):
        return self.symbol
