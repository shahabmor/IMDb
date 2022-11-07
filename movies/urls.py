from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("movies/", movie_list, name='home'),
    path('movie/<int:pk>', movie_detail, name='movie_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
