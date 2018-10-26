""""""
"""

Когда запрашивает страница, Django создает объект HttpRequest, который содержит различные данные о запросе. 
Потом Django определяет и загружает необходимое представление и вызывает его передавая объект HttpRequest первым аргументом. 
Каждое представление должно вернуть объект HttpResponse.


request - ето обьект

Request.GET - QueryDict: {}>    Объект с интерфейсом словаря, который содержит HTTP GET параметры.


Request.POST - ueryDict: {}>   Объект с интерфейсом словаря, который содержит все HTTP POST параметры.

Запрос может использовать метод POST но содержать пустой словарь POST – например, форма была передана через POST HTTP метод, но не содержала 
никаких данных. 
Поэтому, вы не должны использовать if request.POST для проверки был ли использован метод POST; 
вместо этого используйте if request.method == "POST" (смотрите ниже).


request.FILES - <MultiValueDict: {}>   Ключи и значения являются строками.


Request.FILES
Информация о загруженых файлах:
Объект с интерфейсом словаря, который содержит все загруженные файлы. 
Каждый ключ в FILES это name из <input type="file" name="" />. 
Каждое значение в FILES это объект UploadedFile.
Заметим, что FILES содержит данные только, если метод запроса POST и <form> содержал enctype="multipart/form-data". 
В другом случае FILES будет содержать пустой словарь.

Request.META
Словарь Python содержащий все доступные HTTP заголовки запроса

request.user  -   Zohan   Добавляется AuthenticationMiddleware: содержит объект AUTH_USER_MODEL представляющий текущего пользователя.
if request.user.is_authenticated():
    ... # Do something for logged-in users.
else:
    ... # Do something for anonymous users.



"""