from django.forms import HiddenInput
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.forms import Form, HiddenInput, ModelForm

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Photo

# Create your views here.

#display all the albums
class HomeView(LoginRequiredMixin, ListView):
    login_url = '/albums/login/'
    template_name = 'index.html'
    context_object_name = 'album_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album_list'] = context['album_list'].filter(user=self.request.user)
        return context

    def get_queryset(self):
        return Album.objects.order_by('-creation_date')

#create a new album
class NewAlbumView(CreateView):
    model = Album
    # form_class = AlbumForm
    fields = ['user', 'title', 'description']
    template_name = 'newalbum.html'
    def get_success_url(self):
        return reverse('album_site:home')
    def get_form(self):
        form = super(NewAlbumView, self). get_form(self.get_form_class())
        form.fields['user'].widget = HiddenInput()
        form.fields['user'].initial = self.request.user
        return form
        
#display a specific album
class AlbumView(DetailView):
    model = Album
    template_name = 'viewalbum.html'


class AlbumPhotoCreateView(CreateView):
    model = Photo
    fields = ['album', 'image', 'description']
    template_name = 'newphoto.html'
    def get_success_url(self):
        return reverse('album_site:home')
    def get_form(self):
        form = super(AlbumPhotoCreateView, self).get_form(self.get_form_class())
        form.fields['album'].queryset = Album.objects.filter(user=self.request.user)
        return form

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['album', 'image', 'description']
    template_name = 'newphoto.html'
    def get_success_url(self):
        return reverse('album_site:current_album', args=[self.object.album.id])

    def get_form(self):
        form = super(PhotoCreateView, self).get_form(self.get_form_class())
        form.fields['album'].widget = HiddenInput()
        form.fields['album'].initial = Album.objects.get(pk=self.kwargs["pk"]) # sketch
        return form

#display a specific photo
class PhotoView(DetailView):
    model = Photo
    template_name = 'viewphoto.html'
    context_object_name = "p"


#delete photo
class DeletePhoto(DeleteView):
    model = Photo
    success_url = reverse_lazy('album_site:home')

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('album_site:home')

class UpdatePhoto(UpdateView):
    model = Photo
    fields = ['album']
    template_name = 'updatephoto.html'
    success_url = reverse_lazy('album_site:home')

    def get_form(self):
        form = super(UpdatePhoto, self).get_form(self.get_form_class())
        form.fields['album'].queryset = Album.objects.filter(user=self.request.user)
        return form;

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('album_site:home')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('album_site:home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('album_site:home')
        return super(RegisterPage, self).get(*args, **kwargs)