from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileCiteForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ['cite']


class ProfileImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'label': ''}))
    class Meta:
        model = Profile

        fields = ['image']
