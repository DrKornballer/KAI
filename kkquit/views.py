from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, time

# Create your views here.
def index(request):
     return render (request, 'kkquit/index.html')

     
    