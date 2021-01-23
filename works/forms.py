from django import forms
from .models import *

class WorkForm(forms.ModelForm) :
    work_to_do = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Add new task...' , "height" : "15px"}))
    class Meta :
        model = Work
        fields = '__all__'
