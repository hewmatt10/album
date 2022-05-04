from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Album, Photo
from .forms import AlbumForm
# Create your views here.

#display all the albums
class HomeView(ListView):
    template_name = 'index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.order_by('-creation_date')

#create a new album
class NewAlbumView(FormView):
    model = Album
    form_class = AlbumForm
    # fields = ['title', 'description']
    template_name = 'newalbum.html'
    success_url = '/albums'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#display a specific album
class AlbumView(DetailView):
    model = Album
    template_name = 'viewalbum.html'


#upload a photo

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['album', 'description', 'image']
    template_name = 'newphoto.html'
    def get_success_url(self):
        return reverse('album_site:current_album', args=[self.object.album.id])

#display a specific photo

