from django.shortcuts import render
from .models import Movie

def index(request):
    return render(request, 'movies/index.html')