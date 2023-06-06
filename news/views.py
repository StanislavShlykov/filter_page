from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news_list.html'
    context_object_name = 'news_list'

class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'
