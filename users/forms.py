from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username doesn't exist")

        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('The password is incorrect')

        return password


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username_validations = {
        'No spaces are allowed': lambda x: not all([e.isspace() for e in x]),
        'The username must contain at least 5 elements': lambda x: len(x) >= 5,
    }
    password_validations = {
        'The password must contain at least 5 elements': lambda x: len(x) >= 5,
        'The password must contain at least 1 uppercase character': lambda x: len(
            [e.isalpha() and e.isupper() for e in x]) >= 1,
        'The password must contain at least one digit': lambda x: any([x.isdigit() for x in x]),
    }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')

        for message, validation in self.username_validations.items():
            if not validation(username):
                raise forms.ValidationError(message)

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        for message, validation in self.password_validations.items():
            if not validation(password):
                raise forms.ValidationError(message)

        return password
