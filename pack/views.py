from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import packsForm

# Create your views here.

def packs_create(request):
    if request.method == "POST":
        form = packsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return render(request, 'pack/packs_add.html')
    else:
        form = packsForm()
        return render(request, 'pack/index.html', {'form': form })

def pack(request):
      if request.method == "POST":
        form = packsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
      else:
        form = packsForm()
        return render(request, 'pack/index.html', {'form': form})
