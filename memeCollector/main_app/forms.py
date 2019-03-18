from django import forms 
from .models import *

class MemeForm(forms.ModelForm): 
    class Meta: 
        model = Meme 
        fields = ['author', 'city'] 

