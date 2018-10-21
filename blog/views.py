from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import Post, Teg

def test(request): # Запрос с браузера упаковывается в обьект request который попал на наш сервер
    print()
    print(request) # печатаем сам обьект request, <WSGIRequest: GET '/blog/blog/'>   (содержит метод и адрес относительный)
    print()
    print(dir(request))
    print()
    print(request.COOKIES) # {'csrftoken': 'BskAsEIPdrzkNobDlf0EzDGZzDkldjrmsEO2p6h9campdU7uRJfs0Rxzju363y23', 'sessionid': 'zqynfq71ddapwu0053y342zte0rfrmha'}
    print(request.COOKIES.get("csrftoken"))
    print()
    print(request.GET) # <QueryDict: {}>
    print()
    print(request.FILES) # <MultiValueDict: {}>
    print(request.POST) # <QueryDict: {}>
    print(request.user)  # Zohan

    return HttpResponse("Hello")

def posts_list(request): # name = "Женя", Запрос с браузера упаковывается в обьект request который попал на наш сервер
    #last_name = "Serduk"
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts":posts}) #таким образом можно передать в шаблон контекст

# Процес наполнения шаблона данными называется - рендеринг

def detail_post(request, slug):  # мы ждем что slug прийдет из имнованной группы символов урла
    post = Post.objects.get(slug__iexact=slug)
    return render(request, "blog/post_details.html", context={"post" : post}) # в контекст доступер slug, который возмем с урла

def tegs_list(request):
     tegs = Teg.objects.all()
     return render(request, "blog/tegs_list.html", context={"tegs":tegs})


def detail_tegs(request, slug):  # мы ждем что slug прийдет из имнованной группы символов урла
    teg = Teg.objects.get(slug__iexact=slug)
    return render(request, "blog/tegs_detail.html", context={"teg": teg})