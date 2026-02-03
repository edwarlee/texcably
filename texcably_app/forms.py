from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': '',
            'placeholder': 'First name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': '',
            'placeholder': 'Last name',
        })
        self.fields['email'].widget.attrs.update({
            'class': '',
            'placeholder': 'Email',
        })
        self.fields['username'].widget.attrs.update({
            'class': '',
            'placeholder': 'Username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': '',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': '',
            'placeholder': 'Confirm Password',
        })
        for field in self.fields:
            if self.errors and field in self.errors:
                self.fields[field].widget.attrs.update({
                    'class': 'error',
                })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': '',
            'placeholder': 'Username',
        })
        self.fields['password'].widget.attrs.update({
            'class': '',
            'placeholder': 'Password',
        })
        self.fields['username'].error_messages.update({
            'required': 'Please enter your username',
            'max_length': 'Username too long'
        })
        self.fields['password'].error_messages.update({
            'required': 'Please enter your password',
            'max_length': 'Password too long'
        })

        if self.errors and 'username' in self.errors:
            self.fields['username'].widget.attrs.update({
                'class': 'error',
            })
        if self.errors and 'password' in self.errors:
            self.fields['password'].widget.attrs.update({
                'class': 'error',
            })