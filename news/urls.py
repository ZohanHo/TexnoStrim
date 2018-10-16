from django.urls import path, re_path
from .views import MyView  # импортировали views.py
from news import views  # импортировали views.py

urlpatterns = [
    path('hello/', views.show_new, name="hello"), # Указуем функцию прописаную в views.py, а именно show_new
    path('redirect/', views.redirect, name="redirect"), # Указуем функцию прописаную в views.py, а именно show_new
    re_path('^detailview/(?P<pk>\d+)/$', MyView.as_view(), name="detailview"), # именованый url можно использовать в шаблоне
]

# name="hello"    это именнованый url (роут), шаблону можно дать имя, для того чтобы url можно было включить в шаблон, через специальный тег url, типа id url
