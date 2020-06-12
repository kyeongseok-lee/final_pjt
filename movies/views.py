from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Movie, Genre

def index(request):
    movies = Movie.objects.order_by('-pk')
    paginator = Paginator(movies, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_number': page_number,
        'page_obj' : page_obj,
    }
    return render(request, 'movies/index.html', context)