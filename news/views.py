"""Контролер - функции которые должы принять обьект запроса и вернуть обьект ответа"""

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import View, DetailView, ListView
from news.models import Article

def show_new(request): # самая простая вьюха, ее нужно добавить в роутер (urls.py)

    # можем посмотреть какой метод что хранит
    print(request.GET)         # <QueryDict: {}> , если в командной строке после hello/ написать ?name=pert то будет <QueryDict: {'name': ['petr']}>
                               # то с QueryDict можем достать что передал нам пользователь в запросе

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

def render_func(request, name="женя", last_name="Сердюк"):
    return render(request, "blabla.html", {"name": name, "last": last_name}) # В словарь могу добавить контекс дополнительный который могу отобразить по имени в шаблоне
    # по умолханию доюавляется контекс с context_processors, можно добавить что то от себя,если мы считаем что хотим видеть какуето переменную в шаблонах

"""class-based view"""

class MyView(DetailView):
    model = Article
    template_name = "detailview.html"

"""
что тут происходит, определяется метод dispath - который определяет с каким методом запрос к нам пришел, 
и вызывает соответствующую ф-цию илбо GET либо POST
"""

def show(request, name="Zohan", last_name="Serduk"):
    return render(request, "content.html",{"name": name, "last": last_name})

class Mylistview(ListView):
    mosels = Article
    template_name = "content.html"

    def dispatch(self, request, *args, **kwargs): # dispath определяет с каким запросом к нам
        self.sort = request.GET.get("sort") # создаем переменную, и сможем после запроса от пользователя в командной строке в request.GET взять со словаря имя sort
        self.search_title = request.GET.get("search_title")
        self.search_text = request.GET.get("search_text")# создаем поле для поиска
        return super(Mylistview, self).dispatch(request, *args, **kwargs) # после чего вызываем super, что бы функция работала стандартно


    def get_queryset(self):  # метод get_queryset, который берет текущую модель и выгребает все
        queryset = Article.objects.all()
        if self.search_text:
            queryset = Article.objects.all().filter(title__icontains=self.search_text)

        if self.search_title:
            queryset = Article.objects.all().filter(text__icontains=self.search_text)


        if self.sort: # сделали проверку если указали sort, сортируем по sort, если нет то стандартный queryset = Article.objects.all()
            queryset = Article.objects.all().order_by(self.sort) # сортирум с помощью order_by по полю sort, проверили сто оно есть
             # можем переопредилить что бы выгребал последние 4

        return queryset # можем переопредилить что бы выгребал последние 4

""" Хотим что бы пользователь сам выьирал по какому полю сортировать, но если sort = abracodabra все упадет, потому пользователю нельзя давать
    писать в запросе что он хочет, для ето существуют Form (формы) где будет выбиратся по какому полю сортировать

"""
