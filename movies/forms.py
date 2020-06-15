from django import forms
from .models import Recommend, Review, Comment

class RecommendForm(forms.ModelForm):
    GENRE_CHOICES = (
	('12', 'Adventure'),
    ('14', 'Fantasy'),
    ('16', 'Animation'),
    ('18', 'Drama'),
    ('27', 'Horror'),
    ('28', 'Action'),
    ('35', 'Comedy'),
    ('36', 'History'),
    ('37', 'Western'),
    ('53', 'Thriller'),
    ('80', 'Crime'),
    ('99', 'Documentary'),
    ('878', 'Science Fiction'),
    ('9648', 'Mystery'),
    ('10402', 'Music'),
    ('10749', 'Romance'),
    ('10751', 'Family'),
    ('10752', 'War'),
    ('10770', 'TV Movie'),
    )
    genre = forms.ChoiceField(choices = GENRE_CHOICES)
    class Meta:
        model = Recommend
        fields = ['genre', 'vote_average']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rank']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

