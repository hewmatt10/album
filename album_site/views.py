from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Album, Photo
# Create your views here.

#display all the albums
class HomeView(ListView):
    template_name = 'index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.all()

#create a new album
class NewAlbumView(FormView):
    template_name = 'newalbum.html'


#display a specific album

#upload a photo

#display a specific photo

