from django import forms

from .models import Skin


class SkinForm(forms.ModelForm):
    class Meta:
        model = Skin
        fields = ['name', 'image', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),  # 'multiple': 'multiple
        }
