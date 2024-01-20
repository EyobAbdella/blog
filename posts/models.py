from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")
    slug = AutoSlugField(populate_from="title", unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    read_time = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        words_per_minute = 200
        total_words = len(self.content.split())
        self.read_time = int(total_words / words_per_minute)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
