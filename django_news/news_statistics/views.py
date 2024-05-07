from django.shortcuts import render
from django.http import HttpResponse
from news.models import News

# Create your views here.
def statistics(request):
    news_list = News.objects.values_list('id', 'header', 'views')
    overall_views = sum([news[2] for news in news_list])
    print(news_list)
    context = {
        'news_list': news_list,
        'overall_views': overall_views
    }
    return render(request, 'statistics.html', context)