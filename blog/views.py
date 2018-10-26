from django.shortcuts import render, get_object_or_404, resolve_url
from django.shortcuts import HttpResponse
from blog.models import Post, Teg
from django.views.generic import View, CreateView
from .utils import ObjDetailMixin


# Запрос с браузера упаковывается в обьект request который попал на наш сервер
def test(request, pku, name): # если мы передаем в атрибут переменную, она попадает как входные параметры, дополнительно с request и попасть она может
                                # или именованая или не именованная, именованая стразу матчится urls /<name>/, неименованная как я понимаю только через
                                # регулярные выражения...
    print(request.GET.get("nick")) # если в строке запроса браузера будет указано /?nick=rambo, то вернет rambo, eсли нет, то None
    print(request.GET.get("name")) # если в строке запроса браузера будет указано /?name=petr, то вернет petr, eсли нет, то None
    print()
    print(request.encoding) # печатаем сам обьект request, <WSGIRequest: GET '/blog/blog/'>   (содержит метод и полный путь без домена)
    print()
    print(dir(request)) # все атрибуты request
    print()
    print(request.COOKIES) # {'csrftoken': 'BskAsEIPdrzkNobDlf0EzDGZzDkldjrmsEO2p6h9campdU7uRJfs0Rxzju363y23', 'sessionid': 'zqynfq71ddapwu0053y342zte0rfrmha'}
    print(request.COOKIES.get("csrftoken"))
    print(request.COOKIES.get("sessionid"))
    print()
    print(request.GET) # <QueryDict: {}> Объект с интерфейсом словаря, который содержит HTTP GET параметры.
    print()
    print(request.FILES) # <MultiValueDict: {}>
    print(request.POST) # <QueryDict: {}>
    print(request.user)  # Zohan   Добавляется AuthenticationMiddleware: содержит объект AUTH_USER_MODEL представляющий текущего пользователя.
    print(request.session)
    print(request.META.get("SERVER_PORT"))
    print(request.get_full_path())

    resp = HttpResponse("Hello {} {}".format(pku, name))   # можно добавить в ответ как в словарь что то
    resp["name"] = "zohan"
    resp["age"] = 36
    print(resp.get("age"))
    return resp

def posts_list(request): # name = "Женя", Запрос с браузера упаковывается в обьект request который попал на наш сервер
    #last_name = "Serduk"
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts":posts}) #таким образом можно передать в шаблон контекст

# Процес наполнения шаблона данными называется - рендеринг

# def detail_post(request, slug):  # мы ждем что slug прийдет из имнованной группы символов урла
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, "blog/post_details.html", context={"post" : post}) # в контекст доступер slug, который возмем с урла

class PostDetail(ObjDetailMixin, View):
    model = Post
    template_name = "blog/post_details.html"
    # def get(self, request, slug): # Определяем у класса View метод get
    #     post = get_object_or_404(Post, slug__iexact=slug) # Метод get_object_or_404 имеет конструкцию (try, except) в try проверяет наличие slug d queryset, если не находит то exccept - (ошибка 404)
    #     post = Post.objects.get(slug__iexact=slug)
    #     return render(request, "blog/post_details.html", context={"post": post})

# def detail_tegs(request, slug):  # мы ждем что slug прийдет из имнованной группы символов урла
#     teg = Teg.objects.get(slug__iexact=slug)
#     return render(request, "blog/tegs_detail.html", context={"teg": teg})

class TegDetail(ObjDetailMixin, View):
    model = Teg
    template_name = "blog/tegs_detail.html"
    # def get(self, request, slug): # Определяем у класса View метод get
    #     #teg = Teg.objects.get(slug__iexact=slug) # ету проверку выполняет get_object_or_404
    #     teg = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, "blog/tegs_detail.html", context={"teg": teg})

def tegs_list(request):
     tegs = Teg.objects.all()
     return render(request, "blog/tegs_list.html", context={"tegs":tegs})


















# class MyCreateView(CreateView):
#     model = Post
#     template_name = "blog/create_post.html" # с помощью какого шаблона показуем форму для отправки формы для создания
#     #fields = ("title", "text")  # указуем список полей которые будут отодражены при выводе формы для заполнения
#     fields = "__all__"  # указуем список полей которые будут отодражены при выводе формы для заполнения (сейчас все)
#
#     def get_success_url(self): # метод который должен вернуть url на который мы редиректим пользователя в случаее успешного создания модели
#         return resolve_url("detail_posts_url", slug=self.object.slug) # имя урла куда нас возвращает после того как создали форму
# # рендерит нас на страницу деталки по именованому урлу, где мы можем благодаря pk=self.object.pk посмотреть именно нами созданую новось
# # так как createview держит текущую внутренюю переменную pk которую мы можем использовать


"""
Словари или ассоциативные масивы, dict

В языке Питон ключом может быть произвольный неизменяемый тип данных:
целые и действительные числа, строки, кортежи. Ключом в словаре не может быть множество,
но может быть элемент типа frozenset: специальный тип данных, являющийся аналогом типа set,
который нельзя изменять после создания.
Значением элемента словаря может быть любой тип данных, в том числе и изменяемый.



dictionary = {"name":4, 4:"name", 5:6, 7:[1, 2, 3], 10:{"key":10, "man":20}}

dictionary["rus" , "belorus"] = "Moskow", "Minsk" # Добавляем в словарь новые данные
dictionary["ukr"] = "kiev"
print(dictionary["ukr"])

# Как можно создавать словари, для небольших словарей
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'} # стандартный метод
Capitals1 = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington') # чеоез dict, ключь равно значение

# Для создания необходимо передать список, каждый элемент которого является кортежем из двух элементов: ключа и значения
Capitals2 = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])

# Для создания из двух одинаковых по длине списков - словаря
Capitals3 = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))

# С помощью данной конструкции можно сделать номерацию для списка, сделав словарь, можно указать с какой по какую, и шаг
Capitals4 = dict(zip(range(2,7),["Russia", "Ukraine", "USA", "Pl", "Bg"]))
print(Capitals4)



print(Capitals)
print(Capitals1)
print(Capitals2)
print(Capitals3)

for i, j in dictionary.items(): # С помощью функции items, можно реребрать все ключи или значения, или то и то
    print(i, j)

key = 'name'
key2 = 4

Удаление обьектов
if key in dictionary:  # Проверка
    del dictionary[key]

try:
    del dictionary[key2]
except KeyError:
        print('There is no element with key "' + key + '" in dict')
print(dictionary)

# Удаление через функцию pop
использование метода pop: A.pop(key).
Этот метод возвращает значение удаляемого элемента, если элемент с данным ключом отсутствует в словаре,
то возбуждается исключение. Если методу pop передать второй параметр, то если элемент в словаре отсутствует,
то метод pop возвратит значение этого параметра.
Это позволяет проще всего организовать безопасное удаление элемента из словаря: A.pop(key, None)
dictionary.pop(10)
print("Удалил через pop", dictionary)


Работа с елементами словаря
print(dictionary[7]) # Получить обьект по ключу

 способ определения значения по ключу — метод get: dictionary.get(key).
Если элемента с ключом get нет в словаре, то возвращается значение None.
В форме записи с двумя аргументами A.get(key, val) метод возвращает значение val,
если элемент с ключом key отсутствует в словаре
(dictionary.get(7))
(dictionary.get(15)) # Возвращает None если ключ не найден

# Запись с двумя аргументами, второй в строке позвращается, если ключ не найден
(dictionary.get(11, "does not exist")) 
"""