from django import forms

from .models import Skin


class SkinForm(forms.ModelForm):
    class Meta:
        model = Skin
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
