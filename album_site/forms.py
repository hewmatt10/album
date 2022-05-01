from django import forms
class AlbumForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)

    def send(self):
        pass
