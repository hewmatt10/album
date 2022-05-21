from django import forms
from django.forms import Form, HiddenInput, ModelForm
from django.contrib.auth.models import User

from .models import Album, Photo

class AlbumForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    def save(self, request):
        print(self.__dict__)
        print(self.request)
        a = Album.objects.create(title=self.data['title'], description = self.data['description'])


# class PhotoForm(forms.Form):
#     album = Album.objects.get(album.id)
#     description = forms.CharField()
#     image = forms.ImageField()
#     def save(self):
#         p = Photo.objects.create(album=self.data['album'], description = self.data['description'], image = self.data['image'])