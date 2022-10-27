from django.contrib import admin
from imdb.models import *

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class CrewAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['description']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Role, RoleAdmin)