from django.db import models
import datetime

# Create your models here.

class Now (models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    smoked_time = models.DateTimeField()