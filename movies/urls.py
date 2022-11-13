from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("", movie_list, name='home'),
    path("all_movies/", all_movies, name='all_movies'),
    path('movie/<int:pk>', movie_detail, name='movie_detail'),
    path('movies/search/', movie_search, name='search'),
    path('movie/add/', add_movie, name='add_movie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
