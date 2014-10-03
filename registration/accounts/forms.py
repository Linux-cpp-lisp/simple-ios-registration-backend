from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(min_length=1, max_length = 30)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
    avatar = forms.ImageField()