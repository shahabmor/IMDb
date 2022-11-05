from django.urls import path

from .views import *

urlpatterns = [
    path("movies/", movie_list, name='movie_list'),
    path('movie/<int:pk>', movie_detail, name='movie_detail')
]