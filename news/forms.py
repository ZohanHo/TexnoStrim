from django import forms
from . models import Article

class Myform(forms.Form): # Класс Form - принимает данные из запроса(в виде текстовых строк),валидирует относительно типа полей, приводит к нужному представлению на языке питон
    search = forms.CharField(required=False) # текстовое поле, required=False - не ртебуется для успешной валидации формы
    sort = forms.ChoiceField(choices=(("id", "ID"), ("pub_date", "Дата создания"), ("title", "Заголовок")), required=False)

    """ChoiceField ето то что соотверствеет select в html формах, выбор одного значения из списка, кортеж-кортежей, 
    первое наше внутренее представление, второе что должен увидеть пользователь
    У формы есть определенные методы, которые дают возможность валидировать данные, проверить правельно зи заполнена форма
    """

    #def clean(self):
        #raise forms.ValidationError("Ошибка которую я создал") # если делаем так, то ето как бцдто пользовательские данные с строке запроса неверны

    """ в самой форме можно сделать свою валидацию данных, через метод clean, который заполняет словарб для cleaned_data
        тоесть is_valid возвращает False? cleaned_data становится пуустым, в ошибку формы кладем то что зарейзили
        в шаблоне посмотреть можно через {{ form.errors }}
    """

    # Работа с Post запросом, определяем для нее форму

#class Vopros(forms.Form):
    #title = [" "]
    #text = [" "]
    #user = [" "]

class Azf(forms.ModelForm):
    class Meta:
        model = Article
        exclude = [""]
