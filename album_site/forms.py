from django import forms
from django.forms import Form, HiddenInput, ModelForm


from .models import Album, Photo

class AlbumForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    def save(self):
        a = Album.objects.create(title=self.data['title'], description = self.data['description'])

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['album', 'description', 'image']
        widgets = {
            'album' : HiddenInput
        }

    def __init__(self, *args, **kwargs):
        print(kwargs)
        self.id = kwargs.pop('pk', None)
        super(PhotoForm, self).__init__(*args, **kwargs)
        print('SUCKY SUCKYYYYYY :(((((((((')
        print(self.id)
        self.initial['album'] = Album.objects.get(pk=self.id)

# class PhotoForm(forms.Form):
#     album = Album.objects.get(album.id)
#     description = forms.CharField()
#     image = forms.ImageField()
#     def save(self):
#         p = Photo.objects.create(album=self.data['album'], description = self.data['description'], image = self.data['image'])