from django.contrib import admin
from .models import Post, Teg # Импортировали модель из текущего каталога

admin.site.register(Post)
admin.site.register(Teg)
