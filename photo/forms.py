from django import forms

from .models import Photo
from django.core.exceptions import ValidationError


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'image_url')


class ChangeImageForm(forms.Form):
    height = forms.IntegerField(label='Высота', required=False)
    width = forms.IntegerField(label='Ширина', required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('height') and not cleaned_data.get('width'):
            raise ValidationError("Fill in one field to submit the form")

    class Meta:
        fields = ('height', 'width')
