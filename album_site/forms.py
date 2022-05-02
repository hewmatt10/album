from django import forms
from .models import Album

class AlbumForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()

    def save(self):
        a = Album.objects.create(title=self.data['title'], description = self.data['description'])