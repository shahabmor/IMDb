from django.shortcuts import render

from movies.models import Movie


# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    content = {
        "movies": movies,
        "user": "Shahab",
        "is_valid": True
    }

    return render(request, 'movies/movie_list.html', context=content)
