from pack.forms import packsForm
from django.urls import path
from . import views

urlpatterns = [
    path("", views.pack, name="packs")
   
]

