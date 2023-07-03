from django import forms
from .models import OpenData

class OpenDataForm(forms.ModelForm):
    class Meta:
        model = OpenData
        fields = (
            'is_published',
            'orgname',
            'orgsokrname',
            'orgpubname',
            'tipe',
            'post',
            'rukfio',
            'orgfunc',
            'index',
            'region',
            'area',
            'town',
            'street',
            'house',
            'latitude',
            'longitude',
            'mail',
            'telephone',
            'fax',
            'telephonedop',
            'url',
            'okpo',
            'ogrn',
            'inn'
        )