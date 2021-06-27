from django.http.response import HttpResponse
from django.forms.forms import Form
from django.shortcuts import render
from django.http.response import HttpResponse
from django.db import models
from kkquit.models import Now
objects = models.manager 
 
# Create your views here.
def smoking_view(request):
        obj = Now.objects.latest("id")
        context = {'timestamp': obj.smoked_time}
        return render(request, 'my_kai_web/smoking_view.html', context)

    