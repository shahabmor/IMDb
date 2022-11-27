from account.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate

from .models import Movie
from .forms import MovieForm, RateMovieForm


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
        'user_login': request.user.is_authenticated,
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
        'comments': movie.comment.filter(is_valid=True),
        'crew': movie.moviecrew_set.all(),
        'user_login': request.user.is_authenticated,
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


def rate_movie(request, pk, rate=None):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    user = User.objects.get(username=request.user.username)

    if request.method == 'GET':
        form = RateMovieForm(instance=movie)
        ctx = {
            'form': form,
            'movie': movie,
        }
        return render(request, 'rate.html', context=ctx)

    elif request.method == 'POST':
        form = RateMovieForm(request.POST, instance=movie)

        if form.is_valid():
            cd = form.cleaned_data.get('rate')
            new_rate = RateMovieForm.objects.create(movie=movie, rate=cd, user=user)
            rate.save()
            