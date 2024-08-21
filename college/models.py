import os
from uuid import uuid4
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        filename = f"{instance.link}.{ext}"
        return os.path.join(self.sub_path, filename)


class News(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(upload_to=PathAndRename("news/"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.SlugField(default="", null=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"link": self.link})

    def clean(self):
        self.link = slugify(self.title)
        if News.objects.filter(link=self.link).exclude(pk=self.pk).exists():
            raise ValidationError(
                {
                    "title": "A news item with this slug already exists. Please choose a different title."
                }
            )

    def save(self, *args, **kwargs):
        if self.pk:
            old_image = News.objects.get(pk=self.pk).image
            if self.image and old_image != self.image:
                old_image.delete(save=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)
