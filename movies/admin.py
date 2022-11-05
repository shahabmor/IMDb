from django.contrib import admin
from movies.models import *


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_valid']
    search_fields = ['name']
    list_filter = ['is_valid']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_valid']
    list_filter = ['is_valid']


class CrewAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'is_valid']
    search_fields = ['first_name', 'last_name']
    list_filter = ['is_valid']

class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    extra = 2
    readonly_fields = ('crew_gender', )

    def crew_gender(self, obj):
        return obj.crew.get_gender_display()


class MovieGenreInline(admin.TabularInline):
    model = Movie.genres.through
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    list_filter = ['is_valid']
    inlines = (MovieCrewInline, MovieGenreInline)
    exclude = ('genres', )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Role, RoleAdmin)
