from django.forms.forms import Form
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, time
from .forms import Now_form

# Create your views here.
def Now (request):
    if request.method == "POST":
        form = Now_form(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return render(request, 'kkquit/nows.html', {'form': form})
    else:
        form = Now_form()
        return render(request, 'kkquit/index.html', {'form': form })



     
    