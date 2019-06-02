from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

from .forms import UserLoginForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thisway')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thisway')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


