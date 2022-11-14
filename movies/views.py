from django.shortcuts import render, HttpResponse, redirect

from movies.models import Movie
from movies.forms import MovieForm

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()[:10]
    content = {
        "movies": movies,
        "user": "shahab",
        "is_valid": True
    }

    return render(request, 'movies/home.html', context=content)


def all_movies(request):
    movies = Movie.objects.all()
    content = {
        "movies": movies,
        "user": "shahab",
        "is_valid": True
    }

    return render(request, 'movies/all_movie.html', context=content)


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
    item = request.POST.get('search_item').strip()
    movies = Movie.objects.filter(title__contains=item)

    content = {
        "movies": movies,
    }
    return render(request, 'movies/search.html', context=content)


def add_movie(request):
    if request.method == 'GET':
        form = MovieForm()
        ctx = {
            'form': form
        }
        return render(request, 'movies/add_movie.html', context=ctx)

    elif request.method == "POST":
        post = MovieForm(request.POST, request.FILES, instance=Movie)
        if post.is_valid:
            post.save()
            return redirect('all_movies')

        return render(request, 'movies/add_movie.html', context=post)


