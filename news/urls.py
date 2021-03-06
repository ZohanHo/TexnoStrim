from django.urls import path, re_path
from .views import *
from news import views  # импортировали views.py


urlpatterns = [
    path('hello/', views.show_new, name="hello"), # Указуем функцию прописаную в views.py, а именно show_new
    path('view/', views.MyView.as_view(), name="view"), # Указуем функцию прописаную в views.py, а именно show_new
    path('templateview/', MyTemplateView.as_view(), name="templateview"), # Указуем функцию прописаную в views.py, а именно show_new
    path('redirect/', views.redirect, name="redirect"), # Указуем функцию прописаную в views.py, а именно show_new
    re_path('^detailview/(?P<pk>\d+)/$', MyDetailView.as_view(), name="detailview"), # именованый url можно использовать в шаблоне
    path('render/', views.render_func, name="render"), #
    path('show/', views.show, name="show"), #
    path('counter/', counter, name="counter"), #
    path('listview/', Mylistview.as_view(), name="listview"), #
    path('listviewnew/', Mylistviewnew.as_view(), name="listviewnew"), #
    path('createview/', MyCreateView.as_view(), name="createview"), # именованый url можно использовать в шаблоне

]

# name="hello"    это именнованый url (роут), шаблону можно дать имя, для того чтобы url можно было включить в шаблон, через специальный тег url, типа id url


# \d+     одна или больше цифр, то же, что и [0-9]+
# /^.../	первый символ в строке
# /...$/	последний символ в строке
# \w+	один или больше alphanumeric-символов, то же, что и [a-zA-Z0-9]+