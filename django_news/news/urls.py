from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name = 'news'),
    path('by-tag/', views.news_by_tag, name = 'news_by_tag'),
    path('<int:news_id>', views.single_news, name = 'single_news')
] 