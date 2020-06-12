import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Movie, Genre

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


def recommend(request):
    today = datetime.date.today()
    # month = today.month
    # day = today.day
    month = 6
    day = 33
    # movie = get_object_or_404(Movie, pk=1)
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
        # 'today': today,
        # 'month': month,
        # 'day': day,
    }
    return render(request, 'movies/recommend.html', context)