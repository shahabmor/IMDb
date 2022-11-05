from django.shortcuts import render, HttpResponse

from movies.models import Movie


# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()[:8]
    content = {
        "movies": movies,
        "user": "shahab",
        "is_valid": True
    }

    return render(request, 'movies/movie_list.html', context=content)


def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return HttpResponse(f"<h1>{movie}</h1>")