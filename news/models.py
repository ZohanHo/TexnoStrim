from django.db import models

class Article(models.Model): # Описание таблиц для базы данных

    title = models.CharField(max_length=255) # в виде атрибутов (переменных) описуем поля
    text = models.TextField() # используем специальные класы которые находятся в models,  и заканчиваются на fild
    pub_date = models.DateField(auto_now_add=True)

# В зависимости какое поле мы описываем оно соответственно будет себя вести, и в админке, и базе, и записыватся и вытаскиватся
# В качестве аргументов можем передавать разные веши, так в DateField можем передать что при создании обьекта будет указыватся текущая дата