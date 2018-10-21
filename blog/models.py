from django.db import models
from django.shortcuts import reverse #

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True ) # db_index=True - индексация для более быстрого поиска
    slug = models.SlugField(max_length=150) # unique=True - уникальность, SlugField - типа чарфилд, но с валидатором (большие маленькие буквы, цыфры, нижнее подчеркивание,дифис и все)
    body = models.TextField(blank=True) # blank=True - поле может быть пкстым
    data_pub = models.DateTimeField(auto_now_add=True) # Текущая дата при сохранении в базе
    tegs = models.ManyToManyField("Teg", blank=True, related_name="posts") # У модли Post появляется поле tegs, при обращенни к tegs получил все всязаные теги, то у модели Teg появляется полу posts (related_name="posts")

    def get_absolute_url(self): # метод который сам генерит ссылку по иненованой области урла, slug,
        return reverse("detail_posts_url", kwargs={"slug":self.slug})  # передаем <a href="{{ post.get_absolute_url }}" class="btn btn-light">Read</a>

    def __str__(self):
        return "{}".format(self.title)

class Teg(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self): # метод который сам генерит ссылку по иненованой области урла, slug,
        return reverse("detail_tegs_url", kwargs={"slug":self.slug})

    def __str__(self):
        return "{}".format(self.title)