from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'album_site'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('newalbum/', views.NewAlbumView.as_view(), name='new_album'),
    path('<int:pk>/', views.AlbumView.as_view(), name='current_album'),
    path('<int:pk>/newphoto', views.PhotoCreateView.as_view(), name='new_photo'),
    path('newphoto/', views.AlbumPhotoCreateView.as_view(), name='new_album_photo'),
    path('<int:album_pk>/photo/<int:pk>', views.PhotoView.as_view(), name='current_photo'),
    path('<int:album_pk>/photo/<int:pk>/delete', views.DeletePhoto.as_view(), name='delete_photo'),
    path('<int:pk>/delete', views.DeleteAlbum.as_view(), name='delete_album'),
]