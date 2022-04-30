from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

#display all the albums
def index(request):
    return HttpResponse('indexview')

#create a new album

#display a specific album

#upload a photo

#display a specific photo

