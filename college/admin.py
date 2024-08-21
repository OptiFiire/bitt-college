from typing import Any
from django.contrib import admin
from django.forms import ValidationError
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "link", "title", "author")
    fields = ("title", "content", "image", "author")

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            form.add_error("title", e)
            return


admin.site.register(News, NewsAdmin)
