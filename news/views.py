"""Контролер - функции которые должы принять обьект запроса и вернуть обьект ответа"""

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import View, DetailView
from news.models import Article

def show_new(request): # самая простая вьюха, ее нужно добавить в роутер (urls.py)

    # можем посмотреть какой метод что хранит
    print(request.GET)         # <QueryDict: {}> , если в командной строке после hello/ написать ?name=pert то будет <QueryDict: {'name': ['petr']}>
                               # то QueryDict можем достать что передал нам пользователь

    # print(request.method)
    # print(request.COOKIES)
    # print(request.session)
    # print(request.user)
    # print(request.META)

    return HttpResponse("Hello")


    # return HttpResponse ("Hello, {}".format(request.GET.get('name')))
    # в функцию передаем парамет строку которую будем возвращать, можем написать QueryDict в ответе. или же изменить другой заголовор HTTP запроса
    # запрос http://127.0.0.1:8000/hello/?name=petr

def redirect(request): # Редиректит на указаный url

    return HttpResponseRedirect("https://www.google.com.ua")


"""class-based view"""

class MyView(DetailView):
    model = Article
    template_name = "detailview.html"

"""
что тут происходит, определяется метод dispath - который определяет с каким методом запрос к нам пришел, 
и вызывает соответствующую ф-цию илбо GET либо POST
"""