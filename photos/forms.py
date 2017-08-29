from django import forms
from photos.models import photo

class PhotoForm(forms.ModelForm):

    class Meta:
        model = photo
        exclude = []