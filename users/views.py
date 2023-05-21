from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, User.objects.get(username=form.cleaned_data['username']))
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


class Login(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


def logout_view(request):
    logout(request)
    return redirect('login')


class Register(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(Register, self).form_valid(form)
