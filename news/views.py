from django.shortcuts import render
from .models import *


def news(request):
    news_data = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'news': news_data, 'title': 'News', 'logo': '/static/logos/news-logo.png'})
