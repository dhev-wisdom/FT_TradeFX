from django.db import models
from django.utils import timezone

class Trader(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=100)
    last_trade_profit = models.IntegerField(default=0)
    total_profit = models.IntegerField(default=0)
    date_joined = models.DateTimeField(default=timezone.now)
    last_trade_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name