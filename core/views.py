from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "auth/signup.html", {"form": form})


def home(request):
    return render(request, "home.html")
