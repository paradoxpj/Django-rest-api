from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    is_open = models.FloatField()
    is_close = models.FloatField()
    volume = models.IntegerField()
    
    def __str__(self):
        return self.ticker