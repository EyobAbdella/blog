from django.urls import path
from . import views


urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("detail/<slug>/", views.BlogDetailView.as_view(), name="detail"),
    path("create/", views.BlogCreateView.as_view(), name="create"),
]
