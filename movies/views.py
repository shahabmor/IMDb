from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate

from .models import Movie
from .forms import MovieForm

# Create your views here.

def movie_list(request):
    movies = Movie.valid.all()[:10]
    content = {
        "movies": movies,
        "user": "shahab",
        "is_valid": True
    }

    return render(request, 'movies/home.html', context=content)


def all_movies(request):

    movies = Movie.valid.all()
    content = {
        "movies": movies,
        "is_valid": True
    }

    if request.method == 'GET':
        return render(request, 'movies/all_movie.html', context=content)

    # add movie if request.method == 'post'
    elif request.method == "POST":
        post = MovieForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()

            return render(request, 'movies/all_movie.html', context=content)

        return render(request, "movies/add_movie.html", context=post)


def movie_detail(request, pk):

    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    content = {
        'movie': movie,
        'comments': movie.comment.all(),
        'crew': movie.moviecrew_set.all(),
        "is_valid": True
    }

    if request.method == "GET":

        return render(request, 'movies/movie_detail.html', context=content)

    # edit movie if request.method == 'post'
    elif request.method == 'POST':
        edited_movie = MovieForm(request.POST, request.FILES, instance=movie)
        if edited_movie.is_valid():
            edited_movie.save()

            return render(request, 'movies/movie_detail.html', context=content)

        return render(request, 'movies/edit_movie.html', context=content)


def movie_search(request):
    item = request.POST.get('search_item').strip()
    movies = Movie.valid.filter(title__contains=item)

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


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    form = MovieForm(instance=movie)
    ctx = {
        "form": form,
        'movie': movie
    }

    return render(request, 'movies/edit_movie.html', context=ctx)


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    movie.is_valid = False
    movie.save()

    return redirect('all_movies')







