import django
django.setup()

from .models import Trader
from django.utils import timezone, timesince
import random
import math

def simulate_profit_loss():
    print("simulate_profit_loss called via cronjob")
    traders = Trader.objects.all()

    for trader in traders:
        profit_or_loss = math.ceil((random.uniform(-10, 10)))
        print(f"Trader {trader.name} balance before function exec: {trader.balance}")
        trader.balance += profit_or_loss
        print(f"Trader {trader.name} balance after function exec: {trader.balance}")
        trader.last_trade_profit = profit_or_loss
        trader.last_trade_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        trader.total_profit = trader.balance - 100
        trader.save()
        print("data saved")


