from django.db import models

# Create your models here.

class Now (models.Model):
    dt = models.DateTimeField()
