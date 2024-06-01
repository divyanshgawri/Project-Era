from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    mobile = forms.CharField(label='Mobile Number', max_length=10)
    new_username = forms.CharField(label='New Username', max_length=100)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
