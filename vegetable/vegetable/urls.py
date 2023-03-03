"""vegetable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from.import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',view.page,name="home"),
    path('get_post/',view.get_post,name="form"),
    path('dish/',view.dish,name="dish"),
    path('about/',view.about,name="about"),
    path('menu/',view.menu,name="menu"),
    path('url',view.sumbitform,name="sumbitform"),
    path('even',view.even,name="even"),
    path('dynmic_page/',view.dynmic_page,name="dynmic_page")
]
