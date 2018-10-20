from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import Post

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

def posts_list(request, name = "Женя"): # Запрос с браузера упаковывается в обьект request который попал на наш сервер
    last_name = "Serduk"
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"name":name, "last_name":last_name, "posts":posts}) #таким образом можно передать в шаблон контекст

# Процес наполнения шаблона данными называется - рендеринг