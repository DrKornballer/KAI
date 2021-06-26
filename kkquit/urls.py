from kkquit.forms import Now_form
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Now, name="Now")
    
]