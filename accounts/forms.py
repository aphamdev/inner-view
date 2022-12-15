from django import forms


####################################################################
# Creates a login form for user to log in with


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


####################################################################
# creates a signup form for users to sign up for the Web application


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        max_length=150, widget=forms.PasswordInput
    )
