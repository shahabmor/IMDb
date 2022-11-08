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

    content = {
        'movie': movie,
        'crew': movie.moviecrew_set.all(),
        "user": "shahab",
        "is_valid": True
    }
    return render(request, 'movies/movie_detail.html', context=content)


def movie_search(request):
    item = request.POST.get('search_item')
    movies = Movie.objects.filter(title__contains=item)

    content = {
        "movies": movies,
    }
    return render(request, 'movies/search.html', context=content)

