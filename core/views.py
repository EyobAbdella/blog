from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm, SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "auth/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomAuthenticationForm()

    return render(request, "auth/login.html", {"form": form})
