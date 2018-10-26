from django.urls import path, re_path
from .views import *  # импортировали views.py
from news import views  # импортировали views.py


urlpatterns = [
    path('test/<pku>/<name>/', test, name="hello"), # Указуем функцию прописаную в views.py, а именно hello
    path('index/', posts_list, name="posts_list_url"), # Указуем функцию прописаную в views.py, а именно posts_list
    path('teg/<slug>/',TegDetail.as_view(), name="detail_tegs_url"), # slug> - в кавычках указутся именнованая група символов
    path('tegs/', tegs_list, name="teg_list_url"),

    #path('detailpost/create/',PostDetail.as_view(), name="detail_posts_url"), # slug> - в кавычках указутся именнованая група символов
    path('detailpost/<slug>/',PostDetail.as_view(), name="detail_posts_url"), # slug> - в кавычках указутся именнованая група символов
]


#'^detailview/(?P<pk>\d+)/$'