"""Контролер - функции которые должы принять обьект запроса и вернуть обьект ответа"""

from django.shortcuts import render, resolve_url
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import View, DetailView, ListView, TemplateView
from news.models import Article
from .forms import Myform, Azf
from django.views.generic.edit import CreateView

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
    return render(request, "blabla.html", context={"name": name, "last": last_name}) # В словарь request.GET могу добавить дополнительный контекс который можно отобразить по имени в шаблоне
    # по умолханию доюавляется контекс с context_processors, можно добавить что то от себя,если мы считаем что хотим видеть какуето переменную в шаблонах

"""class-based view"""

class MyView(View): # Просто рендерит шаблон

    def get(self, request, name="женя", last_name="Сердюк"):
        return render(request, "news/view.html", context={"name": name, "last": last_name})

# TemplateView - Рендерит шаблон с контекстом который мы ему подготовили, с помощью метода get_context_data
class MyTemplateView(TemplateView):
    template_name = "news/templateview.html"

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        queryset = Article.objects.all() # кверисет ето - список
        q = queryset[0] # причваиваем переменной q -  нулевой елемент списка (обьект модели)
        q.title = "LALALALALA" # через точечную нотацию прискаиваем title новое значение
        q.save() # сохраняем
        c = Article.objects.filter(id="2")
        d = Article.objects.filter(title__icontains="LALALALALA") # Выбрать все обьекты где id содержит слово id
        # for i in range(10): # использовал цыкл до 10
        #     a = Article(title = "title {}".format(i), text="text {}".format(i)) # в каждой итерации создаю новость
        #     a.save() # метод save смотрит по id есть ли такая модель, если нету то создает, если есть то обновлят
        context["question_0"] = q
        context["id1"] = c
        context["title"] = d
        context["question_1"] = queryset[1]
        context["article"] = queryset
        context["nickname"] = "John"
        return context


class MyDetailView(DetailView):
    model = Article
    template_name = "detailview.html"
    context_object_name = "object_detail"  # таким способом можно переименовать тандарный object в свое название, тут object_detail

"""
что тут происходит, определяется метод dispath - который определяет с каким методом запрос к нам пришел, 
и вызывает соответствующую ф-цию илбо GET либо POST, также вызывается метод get, get_template, get_model и отрисовует шаблон
"""


def show(request, name="Zohan", last_name="Serduk"):
    return render(request, "content.html", context={"name": name, "last": last_name})


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

        if self.search_title:
            queryset = queryset.filter(title__icontains=self.search_title)

        if self.search_text:
            queryset = queryset.filter(text__icontains=self.search_text)

        if self.sort: # сделали проверку если указали sort, сортируем по sort, если нет то стандартный queryset = Article.objects.all()
            queryset = queryset.order_by(self.sort) # сортирум с помощью order_by по полю sort, проверили сто оно есть
             # можем переопредилить что бы выгребал последние 4

        return queryset # можем переопредилить что бы выгребал последние 4

""" Хотим что бы пользователь сам выьирал по какому полю сортировать, но если sort = abracodabra все упадет, потому пользователю нельзя давать
    писать в запросе что он хочет, для ето существуют Form (формы) где будет выбиратся по какому полю сортировать и пользователь введя что то
    в строке запроса все не поламает, валидируется все на сервере
"""
class Mylistviewnew(ListView):
    mosels = Article
    template_name = "content.html"

    def dispatch(self, request, *args, **kwargs): # dispath определяет с каким запросом к нам
        # self.sort = request.GET.get("sort") # создаем переменную, и сможем после запроса от пользователя в командной строке в request.GET взять со словаря имя sort
        # self.search_title = request.GET.get("search_title")
        # self.search_text = request.GET.get("search_text")# создаем поле для поиска
        self.form = Myform(request.GET) # Создаем переменную в которую кладем весь масив request.GET, а именно даннные которые пришли от пользователя в строке запроса
        self.form.is_valid() # метод проверяет соответствуют ли данные той форме которую мы прописали, после чего можем оперировать таким атрибутом как cleaned_data
        self.vopros = Azf(request.POST or None) # Создали переменную для работы с POST
        return super(Mylistviewnew, self).dispatch(request, *args, **kwargs) # после чего вызываем super, что бы функция работала стандартно


    def get_queryset(self):  # метод get_queryset, который берет текущую модель и выгребает все
        queryset = Article.objects.all()

        if self.form.cleaned_data.get("search"): # после вызова метода is_valid, заполняется атрибут cleaned_data, с него можем вытащить search
            queryset = queryset.filter(title__icontains=self.form.cleaned_data["search"])

        if self.form.cleaned_data.get("sort"): #
            queryset = queryset.order_by(self.form.cleaned_data["sort"]) # сортирум с помощью order_by по полю sort, проверили сто оно есть
        return queryset # можем переопредилить что бы выгребал последние [:4]

    """Можем переопредилить метод get_context_data - ето метод который вызывается у любого класса View и кторый составляет словарик
    отправляющийся в шаблон для рендера"""

    def get_context_data(self, **kwargs):
        context = super(Mylistviewnew, self).get_context_data(**kwargs) # вызываем метод у родителя
        context["form"] = self.form # добавляем нашу форму, кторая потом доступна в шаблоне
        context["vopros"] = self.vopros # добавляем нашу форму, кторая потом доступна в шаблоне
        return context

    """Для работы с POST запросом необходимо использовать функцию CreateView
    """
class MyCreateView(CreateView):
    model = Article
    template_name = "create.html" # с помощью какого шаблона показуем форму для отправки формы для создания
    #fields = ("title", "text")  # указуем список полей которые будут отодражены при выводе формы для заполнения
    fields = "__all__"  # указуем список полей которые будут отодражены при выводе формы для заполнения (сейчас все)

    def get_success_url(self): # метод который должен вернуть url на который мы редиректим пользователя в случаее успешного создания модели
        return resolve_url("detailview", pk=self.object.pk) # имя урла куда нас возвращает после того как создали форму
# рендерит нас на страницу деталки по именованому урлу, где мы можем благодаря pk=self.object.pk посмотреть именно нами созданую новось
# так как createview держит текущую внутренюю переменную pk которую мы можем использовать


"""Получение числа визитов"""

def counter(request):
    num_article = Article.objects.count()  # Чило воностей на сайте
    num_visits = request.session.get('num_visits', 0) # Хотим получить число визитов, если их нету то говорим что равно 0
    request.session['num_visits'] = num_visits + 1 # в request.session  увиличиваем num_visits на 1 при каэдом обновлении страницы
    return render(
        request,
        'counts.html',
        context={'num_article': num_article,
                 'num_visits': num_visits},
    )