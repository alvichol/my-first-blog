from django.shortcuts import render
from django.utils import timezone
from .models import Post   # мы импортируем модель (Post) из models.py


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # мы создали переменную posts для QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts})

# мы создали функцию (def) с именем post_list, которая принимает request в качестве аргумента
# и возвращает (return) результат работы функции render,
# которая уже соберёт наш шаблон страницы blog/post_list.html

# В функции render у нас есть параметр request
# (т.е. всё, что мы получим от пользователя в качестве запроса через Интернет)
# и файл шаблона 'blog/post_list.html'.

# Последний параметр, который выглядит как {}, — это место, куда мы можем добавить что-нибудь
# для использования в шаблоне. Мы должны задавать имена передаваемым шаблону вещам
# (прямо сейчас мы остановимся на 'posts' :)). В итоге параметр будет выглядеть
# следующим образом: {'posts': posts}. Обрати внимание, что часть перед :
# является строкой; её нужно обернуть в кавычки ''.
