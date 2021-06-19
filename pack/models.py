from django.db import models
import datetime

# Create your models here.

class packs (models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    num_packs = models.SmallIntegerField(max_length=10)
    cost_packs = models.DecimalField(max_digits=6, decimal_places=2)

