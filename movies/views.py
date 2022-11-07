from django.shortcuts import render, HttpResponse

from movies.models import Movie


# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()[:10]
    content = {
        "movies": movies,
        "user": "shahab",
        "is_valid": True
    }

    return render(request, 'movies/home.html', context=content)


def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    crew = movie.crew.all()

    content = {
        'movie': movie,
        'crew': movie.moviecrew_set.all(),
        'role': "",
        "user": "shahab",
        "is_valid": True
    }
    return render(request, 'movies/movie_detail.html', context=content)