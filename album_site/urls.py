from django.urls import path

from . import views


app_name = 'albumapp'
urlpatterns = [
    path('', views.index, name='index'),
]