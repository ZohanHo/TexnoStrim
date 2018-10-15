from django.contrib import admin
from .models import Article # Импортировали модель из текущего каталога

admin.site.register(Article) # регистрауия модели с помощью функции

