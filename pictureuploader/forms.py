from django import forms
from .models import Image
class imageForms(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo': ''}