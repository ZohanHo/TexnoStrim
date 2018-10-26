from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

from blog.models import Post, Teg



class ObjDetailMixin:
    model = None
    template_name = None

    def get(self, request, slug): # Определяем у класса View метод get
        obj = get_object_or_404(self.model, slug__iexact=slug) # Метод get_object_or_404 имеет конструкцию (try, except) в try проверяет наличие slug d queryset, если не находит то exccept - (ошибка 404)
        #post = Post.objects.get(slug__iexact=slug)
        return render(request, self.template_name, context={self.model.__name__.lower(): obj})