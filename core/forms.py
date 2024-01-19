from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-content"}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-content"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-content"}),
    )

    class Meta:
        model = User
        fields = ("email", "full_name", "password1", "password2", "image")

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-content"}),
            "image": forms.ClearableFileInput(attrs={"class": "image-content"}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-content"
        self.fields["password"].widget.attrs["class"] = "form-content"
