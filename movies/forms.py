from django import forms
from .models import Movielist, Review, Comment

class MovielistForm(forms.ModelForm):
    GENRE_CHOICES = (
	('12', "\ubaa8\ud5d8"),
    ('14', "\ud310\ud0c0\uc9c0"),
    ('16', "\uc560\ub2c8\uba54\uc774\uc158"),
    ('18', "\ub4dc\ub77c\ub9c8"),
    ('27', "\uacf5\ud3ec"),
    ('28', "\uc561\uc158"),
    ('35', "\ucf54\ubbf8\ub514"),
    ('36', "\uc5ed\uc0ac"),
    ('37', "\uc11c\ubd80"),
    ('53', "\uc2a4\ub9b4\ub7ec"),
    ('80', "\ubc94\uc8c4"),
    ('99', "\ub2e4\ud050\uba58\ud130\ub9ac"),
    ('878', "SF"),
    ('9648', "\ubbf8\uc2a4\ud130\ub9ac"),
    ('10402', "\uc74c\uc545"),
    ('10749', "\ub85c\ub9e8\uc2a4"),
    ('10751', "\uac00\uc871"),
    ('10752', "\uc804\uc7c1"),
    ('10770', "TV \uc601\ud654"),
    )
    genre = forms.ChoiceField(choices = GENRE_CHOICES)
    class Meta:
        model = Movielist
        fields = ['genre', 'vote_average']
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rank']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

