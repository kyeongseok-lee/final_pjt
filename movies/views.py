from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Movie, Genre, Review, Comment, Movielist
from .forms import MovielistForm, ReviewForm, CommentForm
from django.db.models import Avg
import datetime


def index(request):
    movies_1 = Movie.objects.order_by('pk')[:10]
    movies_2 = Movie.objects.order_by('pk')[10:20]
    movies_3 = Movie.objects.order_by('pk')[20:30]
    context = {
        'movies_1': movies_1,
        'movies_2': movies_2,
        'movies_3': movies_3,
    }
    return render(request, 'movies/index.html', context)



@login_required
def movie_form(request):
    if request.method == 'POST':
        form = MovielistForm(request.POST)
        if form.is_valid():
            movielist = form.save()
            return redirect('movies:movie_list', movielist.pk)
    else:
        form = MovielistForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/movie_form.html', context)


@login_required
def movie_list(request, movielist_pk):
    movielist = Movielist.objects.get(pk=movielist_pk)
    movies = Movie.objects.filter(genres=movielist.genre, vote_average__gte=movielist.vote_average)

    paginator = Paginator(movies, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_number': page_number,
        'page_obj' : page_obj,
    }
    return render(request, 'movies/movie_list.html', context)

   
@login_required
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    avg_rank = reviews.aggregate(Avg('rank'))['rank__avg']
    # avg_rank = avg_ranks[rank_avg]
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
        'avg_rank': avg_rank,
    }
    return render(request, 'movies/movie_detail.html', context)


@login_required
def movie_like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.users_like.filter(pk=user.pk).exists():
        movie.users_like.remove(user)
        liked = False
    else:
        movie.users_like.add(user)
        liked = True
    context = {
        'liked': liked,
        'count': movie.users_like.count(),
    }
    return JsonResponse(context)


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
        return render(request, 'movies/update.html', context)
    else:
        return redirect('movies:movie_detail', movie_pk)


@require_POST
@login_required
def delete_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:movie_detail', movie_pk)


@login_required
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    review.movie = movie
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('movies:review_detail', movie_pk, review_pk)
    else:    
        form = CommentForm()
    context = {
        'form': form,
        'review': review,
        'movie': movie,
    }
    return render(request, 'movies/review_detail.html', context)


@login_required
def review_like(request, movie_pk, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    if review.users_like.filter(pk=user.pk).exists():
        review.users_like.remove(user)
        liked = False
    else:
        review.users_like.add(user)
        liked = True
    context = {
        'liked': liked,
        'count': review.users_like.count(),
    }
    return JsonResponse(context)
    

@login_required
def update_comment(request, movie_pk, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('movies:review_detail', movie_pk, review_pk)
        else:
            form = CommentForm(instance=comment)
        context = {
            'form': form,
        }
        return render(request, 'movies/update.html', context)
    else:
        return redirect('movies:review_detail', movie_pk, review_pk)


@require_POST
@login_required
def delete_comment(request, movie_pk, review_pk, comment_pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:review_detail', movie_pk, review_pk)


@login_required
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



