from django import forms
from .models import Song, Album

class SongCreateForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['name', 'genre', 'music']
