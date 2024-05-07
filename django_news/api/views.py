from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import NewsSerializer
from rest_framework.response import Response
from news.models import News, Tag

@api_view(['GET'])
def api_overview(request):
    api_overview = {
        'Get Single News [GET]': '/get_single/<int:id>',
        'Get Multiple News [GET]': 'get_multiple/<int:start>/<int:end>',
        'Create news [POST]': 'create (data: { "header": header, "text": text, "image": image(file), "tags": "tag1, tag2" }',
        'Like a news [POST]': 'like/<int:news_id>',
        'Dislike a news [POST]': 'dislike/<int:news_id>',
        'Add view to a news [POST]': 'view/<int:news_id>',
        'Delete a news [DELETE]': 'delete/<int:news_id>',
    }
    return Response(api_overview)

@api_view(['GET'])
def get_single_news(request, id):
    news = News.objects.filter(id = id).first()
    if news: return Response(news.dict())
    else: return Response(status = 404)

@api_view(['GET'])
def get_multiple_news(request, start, end):
    request_object = dict(request.GET)
    return_object = []
    
    if 'tags' in request_object and request_object['tags'] != ['']:
        tag_list = []
        for raw_tag in request_object['tags'][0].split(','):
            filtered_tag_name = raw_tag.lower().replace(' ', '')
            tag_list.append(Tag.objects.filter(tag_name = filtered_tag_name).first())
            
        
        news = News.objects.filter(tags__in = tag_list).order_by('-id').all()[start:end]
        print(len(news))
    else:
        news = News.objects.order_by('-id').all()[start:end]
        
    for news_ in news: return_object.append(news_.dict())
    return Response(return_object)

@api_view(['POST'])
def create_news(request):
    print(request.data)
    news = NewsSerializer(data = request.data)
    if news.is_valid():
        if 'tags' in request.data:
            tag_list = []
            tag_name_list = request.data['tags'].lower().replace(' ', '').split(',')
            for tag_name in tag_name_list:
                tag = Tag.objects.filter(tag_name = tag_name).first()
                if not tag:
                    tag = Tag(tag_name = tag_name)
                    tag.save()
                tag_list.append(tag)
    
        news_object: News = news.save()
        news_object.tags.add(*tag_list)
        
        return Response(status = 200)
    return Response(status = 400)

@api_view(['POST'])
def like(request, news_id):
    news = News.objects.filter(id = news_id).first()
    if news:
        news.likes += 1
        news.save()
        return Response(status = 200)
    else: return Response(status = 400)

@api_view(['POST'])
def dislike(request, news_id):
    news = News.objects.filter(id = news_id).first()
    if news:
        news.dislikes += 1
        news.save()
        return Response(status = 200)
    else: return Response(status = 400)
    
@api_view(['DELETE'])
def delete(request, news_id):
    news = News.objects.filter(id = news_id).first()
    if news:
        news.delete()
        return Response(status = 200)
    else:
        return Response(status = 400)

@api_view(['POST'])
def add_view(request, news_id):
    news = News.objects.filter(id = news_id).first()
    if news:
        news.views += 1
        news.save()
        return Response(status = 200)
    else:
        return Response(status = 404)