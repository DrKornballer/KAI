from kkquit.forms import Now_form
from django.urls import path
from . import views
from kkquit.views import smoking_view

urlpatterns = [
    path("", views.Now, name="kkquit"),
    path('now/', views.smoking_view, name="smoking_view"),    
]