from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import News


def newsList(request):
    newsList = News.objects.all()
    return render(request, "news/news_list.html", {"newsList": newsList})


def newsDetail(request, slug):
    newsInfo = News.objects.get(link=slug)
    return render(request, "news/news_detail.html", {"newsInfo": newsInfo})


def home(request):
    lastNews = News.objects.all()[:3]
    return render(request, "home.html", {"news": lastNews})
