from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movieform/', views.movie_form, name='movie_form'),  
    path('movieform/<int:movielist_pk>/list/', views.movie_list, name='movie_list'),  
    path('recommend/', views.recommend, name='recommend'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/like/', views.movie_like, name='movie_like'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.update_review, name='update_review'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
    path('<int:movie_pk>/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/<int:review_pk>/like/', views.review_like, name='review_like'),
    path('<int:movie_pk>/<int:review_pk>/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    path('<int:movie_pk>/<int:review_pk>/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]

