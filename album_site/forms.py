from django import forms

class AlbumForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    