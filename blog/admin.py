from django.contrib import admin
from .models import Post # Импортировали модель из текущего каталога

admin.site.register(Post)