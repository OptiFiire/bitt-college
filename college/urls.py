from django.urls import path
from .views import newsList, newsDetail

urlpatterns = [
    path("<slug:slug>", newsDetail, name="newsDetail"),
    path("", newsList, name="newsList"),
]