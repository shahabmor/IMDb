from django.contrib import admin
from imdb.models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Crew)
admin.site.register(MovieCrew)
admin.site.register(Role)