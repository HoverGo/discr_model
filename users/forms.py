from django import forms
from .models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Write username',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        'placeholder': 'Write password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
