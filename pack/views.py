from django.shortcuts import render
from .forms import packsForm

# Create your views here.

def packs_create(request):
     form=packsForm(request.POST or None)
     if form.is_valid():
          form.save()
     
     return render(request, 'pack/index.htmnl')
     
def pack(request):
     return render(request, 'pack/index.html')
