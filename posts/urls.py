from django.urls import path
from . import views


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="home"),
    path("detail/<slug>/", views.ArticleDetailView.as_view(), name="detail"),
    path("create/", views.ArticleCreateView.as_view(), name="create"),
]
