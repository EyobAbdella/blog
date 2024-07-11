from django.forms import BaseModelForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm
from .models import Article, Category


class BlogListView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all()


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog-create.html"
    form_class = ArticleForm

    def get_success_url(self):
        return reverse("detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog-detail.html"
    context_object_name = "article"
