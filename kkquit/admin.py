from kkquit.models import Now
from django.contrib import admin

class Now_admin(admin.ModelAdmin):
    list_display = ["id", "timestamp"]
# Register your models here.
admin.site.register(Now, Now_admin)