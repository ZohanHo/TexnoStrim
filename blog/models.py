from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True ) # db_index=True - индексация для более быстрого поиска
    slug = models.SlugField(max_length=150) # unique=True - уникальность, SlugField - типа чарфилд, но с валидатором (большие маленькие буквы, цыфры, нижнее подчеркивание,дифис и все)
    body = models.TextField(blank=True) # blank=True - поле может быть пкстым
    data_pub = models.DateTimeField(auto_now_add=True) # Текущая дата при сохранении в базе

    def __str__(self):
        return "{}".format(self.title)