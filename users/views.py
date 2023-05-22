from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import LoginForm, RegisterForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, User.objects.get(username=form.cleaned_data['username']))
            return redirect('posts')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('posts')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')
