from django.urls import path
from . import views
import my_kai_web

urlpatterns = [
    path("", views.smoking_view, name="my_kai_web"),
]