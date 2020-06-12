from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                # return redirect(request.GET.get('next') or 'movies:hello')
                return redirect('accounts:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }        
        return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('accounts:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


@login_required
def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)

    if user != request.user:
        if request.user in user.followers.all():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('accounts:profile', user.username)
