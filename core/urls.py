from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("blog", views.home, name="home"),
]
