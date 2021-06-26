from pack.models import packs
from django.contrib import admin
from .models import packs

class packs_admin(admin.ModelAdmin):
    list_display = ["id", "num_packs", "timestamp", "cost_packs"]
# Register your models here
admin.site.register(packs, packs_admin),

