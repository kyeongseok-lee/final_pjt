from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Review, Comment
from .forms import ReviewForm, CommentForm
import datetime


def index(request):
    movies = Movie.objects.order_by('pk')[:6]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()
    reviews = Review.objects.order_by('-pk')
    context = {
        'movie': movie,
        'form': form,
        'reviews': reviews,
    }
    return render(requestm, 'movies/movie_detail.html', context)


def recommend(request):
    today = datetime.date.today()
    month = today.month
    day = today.day
    movies_todays = Movie.objects.filter(
        release_date__month=month,
        release_date__day=day
    )
    movies_day = Movie.objects.filter(release_date__day=day).order_by('pk')[:5]
    movies_month = Movie.objects.filter(release_date__month=month).order_by('pk')[:5]
    context = {
        'movies_todays': movies_todays,
        'movies_month': movies_month,
        'movies_day': movies_day,
    }
    return render(request, 'movies/recommend.html', context)


