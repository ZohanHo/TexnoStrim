"""TexnoStrim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import auth_login, auth_logout
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tehno/', include("news.urls"), name="news"), # Указуем urls который продоллжит обработку urls адресов
    path('blog/', include("blog.urls"), name="blog"), # Указуем urls который продоллжит обработку urls адресов

    #path('login/', login, {"template_name": "login.html"}), # login импотрируем, и прописуем в шаблоне для него форму

    path('accounts/', include('django.contrib.auth.urls')),
    #re_path(r'^login/$', views.login, name='login'),
    #path('logout/', logout, {"template_name": "login.html"}), # login импотрируем, и прописуем в шаблоне для него форму
]
