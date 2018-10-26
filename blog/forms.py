from django import forms
from . models import *


class TegForm(forms.ModelForm): # form теги html в джанго наз. виджеты
    class Meta:
        model = Post
        exclude = [""]
