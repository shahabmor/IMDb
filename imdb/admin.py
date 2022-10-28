from django.contrib import admin
from imdb.models import *


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['is_valid']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['is_valid']


class CrewAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['is_valid']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Role, RoleAdmin)
