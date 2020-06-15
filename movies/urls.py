from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk/create_review/', views.create_review, name='create_review')
    path('<int:movie_pk/<int:review_pk>/update/', views.update_review, name='update_review'),
    path('<int:movie_pk/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
]

