from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms


class Article(models.Model): # Описание таблиц для базы данных

    title = models.CharField(max_length=255) # в виде атрибутов (переменных) описуем поля
    text = models.TextField() # используем специальные класы которые находятся в models,  и заканчиваются на fild
    pub_date = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=255)

    def __str__(self):
        return "Наш id = {}".format(self.id)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы "
        ordering = ("-pub_date", ) # сортировка что бы почать всегда вопросы по дате в обратном порядке

# В зависимости какое поле мы описываем оно соответственно будет себя вести, и в админке, и базе, и записыватся и вытаскиватся
# В качестве аргументов можем передавать разные веши, так в DateField можем передать что при создании обьекта будет указыватся текущая дата


