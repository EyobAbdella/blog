from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "image", "content", "category"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "title-input", "placeholder": "Enter Blog Title"}
            ),
            "category": forms.Select(attrs={"class": "select-category"}),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Category"
