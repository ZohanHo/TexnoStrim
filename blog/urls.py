from django.urls import path, re_path
from .views import posts_list, test, detail_post, detail_tegs, tegs_list  # импортировали views.py
from news import views  # импортировали views.py


urlpatterns = [
    path('test/', test, name="hello"), # Указуем функцию прописаную в views.py, а именно hello
    path('index/', posts_list, name="posts_list_url"), # Указуем функцию прописаную в views.py, а именно posts_list
    path('detailpost/<slug>/',detail_post , name="detail_posts_url"), # slug> - в кавычках указутся именнованая група символов
    path('teg/<slug>/',detail_tegs , name="detail_tegs_url"), # slug> - в кавычках указутся именнованая група символов
    path('tegs/', tegs_list, name="teg_list_url"),
]


