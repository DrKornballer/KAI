from django.shortcuts import render

# Create your views here.

def pack(request):
     return render(request, 'pack/index.html')
