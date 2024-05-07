from django.shortcuts import render
from django.http import Http404
from .models import News

# Create your views here.
def news(request):
    return render(request, 'all-news.html')

# Create your views here.
def news_by_tag(request):
    return render(request, 'news-by-tag.html')

# Create your views here.
def single_news(request, news_id):
    news = News.objects.filter(id = news_id).first()
    if news:
        context = { 'news_id': news.id, 'header': news.header, 'text': news.text, 'image': news.image.url, 'tags': news.tags.all()}
        return render(request, 'single-news.html', context)