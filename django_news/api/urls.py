from django.urls import path 
from . import views

urlpatterns = [
    path('', views.api_overview, name = 'api_overview'),
    path('get_single/<int:id>', views.get_single_news, name = 'get_single_news'),
    path('get_multiple/<int:start>/<int:end>', views.get_multiple_news, name = 'get_multiple_news'),
    path('like/<int:news_id>', views.like, name = 'like'),
    path('dislike/<int:news_id>', views.dislike, name = 'like'),
    path('view/<int:news_id>', views.add_view, name = 'add_view'),
    path('delete/<int:news_id>', views.delete, name = 'like'),
    path('create', views.create_news, name = 'create_news'),
]