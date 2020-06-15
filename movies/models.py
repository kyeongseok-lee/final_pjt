from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name='movies')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)

class Movielist(models.Model):
    genre = models.CharField(max_length=100)
    vote_average = models.IntegerField()