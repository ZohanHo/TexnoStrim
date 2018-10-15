"""Контролер - функции которые должы принять обьект запроса и вернуть обьект ответа"""

from django.shortcuts import render
from django.shortcuts import HttpResponse

def show_new(request): # самая простая вьюха, ее нужно добавить в роутер (urls.py)

    # можем посмотреть какой метод что хранит
    print(request.GET)         # <QueryDict: {}> , если в командной строке после hello/ написать ?name=pert то будет <QueryDict: {'name': ['petr']}>
                               # то QueryDict можем достать что передал нам пользователь

    # print(request.method)
    # print(request.COOKIES)
    # print(request.session)
    # print(request.user)
    # print(request.META)

    return HttpResponse ("Hello, {}".format(request.GET.get('name'))) # в функцию передаем парамет строку которую будем возвращать, можем написать QueryDict в ответе
    # запрос http://127.0.0.1:8000/hello/?name=petr

