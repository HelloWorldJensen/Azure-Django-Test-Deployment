from django.db import models

class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=3)

    def __str__(self):
        return self.symbol
