from django.forms.forms import Form
from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import Now_form
from django.db import models
from .models import Now as Now
 

# Create your views here.
def smoking_view(request):
        obj = Now.objects.all(),
        context = {'timestamp' : obj.smoked_time}
        return render(request, 'kkquit/smoking_view.html', context)

def Now (request):
    if request.method == "POST":
        form = Now_form(request.POST)
        if form.is_valid():
            form.save(commit = True)
        return render(request, 'kkquit/nows.html')
    else:
        form = Now_form()
        return render(request, 'kkquit/index.html', {'form': form })




     
    