from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('members:profile', id=user.profile.id)
    else:
        form = AuthenticationForm()
    return render(request, 'members/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('main:index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            messages.success(request, f'Welcome, to the club, {user.username}!')
            messages.add_message(request, messages.INFO, 'You have been registered successfully!')
            return redirect('members:profile', id=profile.id)
    form = UserCreationForm()
    return render(request, 'members/signup.html', {'form': form})

@login_required
def profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    context = {
        'profile': profile
    }
    return render(request, 'members/profile.html', context)