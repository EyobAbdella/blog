from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "category"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "title-input", "placeholder": "Enter Blog Title"}
            ),
        }
