from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Review, Comment
from .forms import ReviewForm, CommentForm
import datetime


def index(request):

    movies = Movie.objects.order_by('pk')
    paginator = Paginator(movies, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_number': page_number,
        'page_obj' : page_obj,

    }
    return render(request, 'movies/index.html', context)


# def movielist(request, movielist_pk):
#     recommend = Recommend.objects.get(pk=recommend_pk)
#     movies = Movie.objects.filter(genres=recommend.genre, vote_average__gte=recommend.vote_average)

#     paginator = Paginator(movies, 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'movies': movies,
#         'page_number': page_number,
#         'page_obj' : page_obj,
#     }
#     return render(request, 'movies/recommend_list.html', context)

#     movies = Movie.objects.order_by('pk')[:6]
#     context = {
#         'movies': movies,
#     }
#     return render(request, 'movies/index.html', context)

@login_required
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.order_by('-pk')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movies:movie_detail', movie_pk)
    else:
        form = ReviewForm()
    context = {
        'movie': movie,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'movies/movie_detail.html', context)


# @login_required
# def create_review(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.movie = movie
#             review.save()
#             return redirect('movies:movie_detail', movie_pk)


@login_required
def update_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('movies:movie_detail', movie_pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            'form': form,
        }
        return render(request, 'movies/update_review.html', context)
    else:
        return redirect('movies:movie_detail', movie_pk)

@require_POST
@login_required
def delete_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:movie_detail', movie_pk)


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



