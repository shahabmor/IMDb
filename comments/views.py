from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from movies.models import Movie
from .models import MovieComment
from account.models import User


def add_comment(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    user = User.objects.get(username=request.user.username)

    if request.method == 'GET':
        form = CommentForm(instance=movie)
        ctx = {
            'form': form,
            'movie': movie,
        }

        return render(request, 'comments/add_comment.html', context=ctx)

    elif request.method == 'POST':
        form = CommentForm(request.POST, instance=movie)

        if form.is_valid():
            cd = form.cleaned_data.get('comment_body')
            new_comment = MovieComment.objects.create(movie=movie, comment_body=cd, user=user)
            new_comment.save()

        content = {
            'movie': movie,
            'crew': movie.moviecrew_set.all(),
            'comments': movie.comment.filter(is_valid=True),
            'user_login': request.user.is_authenticated,
            "is_valid": True
        }

        return render(request, 'movies/movie_detail.html', context=content)


def movie_comments(request, pk):
    the_comment = get_object_or_404(MovieComment, pk=pk, is_valid=True)
    user = User.objects.get(username=request.user.username)
    movie = the_comment.movie

    if request.method == 'GET':
        form = CommentForm()

        ctx = {
            'the_comment': the_comment,
            'all_replies': [],
            'form': form,
            'movie': movie,
        }

        return render(request, 'comments/movie_comments.html', context=ctx)

    elif request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data.get('comment_body')
            reply = MovieComment.objects.create(movie=movie, comment_body=cd, user=user, parent=the_comment)
            reply.save()

        content = {
            'movie': movie,
            'crew': movie.moviecrew_set.all(),
            'comments': movie.comment.filter(is_valid=True),
            'user_login': request.user.is_authenticated,
            "is_valid": True
        }

        return render(request, 'movies/movie_detail.html', context=content)


def comment_delete(request, pk):
    comment = get_object_or_404(MovieComment, pk=pk, is_valid=True)
    access = (request.user.username == comment.user.username)

    if access:
        comment.is_valid = False
        comment.save()

    ctx = {
        'movie': comment.movie,
        'crew': comment.movie.moviecrew_set.all(),
        'comments': comment.movie.comment.filter(is_valid=True),
        'user_login': request.user.is_authenticated,
        "is_valid": True
    }

    return render(request, 'movies/movie_detail.html', context=ctx)


def edit_comment(request, pk):

    comment = get_object_or_404(MovieComment, pk=pk, is_valid=True)
    movie = comment.movie

    access = (request.user.username == comment.user.username)

    if request.method == 'GET':
        if access:
            form = CommentForm(instance=comment)

            ctx = {
                'form': form,
                'movie': movie,
                'comment': comment,
            }

            return render(request, 'comments/edit_comment.html', context=ctx)

        content = {
            'movie': movie,
            'crew': movie.moviecrew_set.all(),
            'comments': movie.comment.filter(is_valid=True),
            'user_login': request.user.is_authenticated,
            "is_valid": True
        }

        return render(request, 'movies/movie_detail.html', context=content)

    elif request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment.comment_body = form.cleaned_data.get('comment_body')
            comment.save()

        content = {
            'movie': movie,
            'crew': movie.moviecrew_set.all(),
            'comments': movie.comment.filter(is_valid=True),
            'user_login': request.user.is_authenticated,
            "is_valid": True
        }

        return render(request, 'movies/movie_detail.html', context=content)

