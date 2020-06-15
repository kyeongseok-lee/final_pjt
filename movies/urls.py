from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movieform/', views.movie_form, name='movie_form'),  
    path('movieform/<int:movielist_pk>/list/', views.movie_list, name='movie_list'),  
    path('recommend/', views.recommend, name='recommend'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.update_review, name='update_review'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
]

