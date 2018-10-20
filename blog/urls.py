from django.urls import path, re_path
from .views import posts_list, test  # импортировали views.py
from news import views  # импортировали views.py


urlpatterns = [
    path('test/', test, name="hello"), # Указуем функцию прописаную в views.py, а именно hello
    path('index/', posts_list, name="posts_list"), # Указуем функцию прописаную в views.py, а именно posts_list
]
