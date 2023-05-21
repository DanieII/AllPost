from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_validations = {
        'The password must contain at least 5 elements': lambda x: len(x) >= 5,
        # 'The password must contain at least 1 uppercase character': lambda x: len(
        #     [e.isalpha() and e.isupper() for e in x]) >= 1,
        # 'The password must contain at least one digit': lambda x: len([x.isdigit() for x in x]) == 1,
    }

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Username doesn\'t exist')

        if len(username) < 5:
            raise forms.ValidationError('Username needs to be at least 5 characters')

    def clean_password(self):
        password = self.cleaned_data['password']
        for message, validation in self.password_validations.items():
            if not validation(password):
                raise forms.ValidationError(message)
