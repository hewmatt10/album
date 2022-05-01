from django.urls import path

from . import views


app_name = 'albumapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('newalbum', views.NewAlbumView.as_view(), name="new_album")
]