from django.forms import ModelForm
from .models import packs

class packsForm(ModelForm):
    class Meta:
        model = packs
        fields = ('num_packs', 'cost_packs')
     

