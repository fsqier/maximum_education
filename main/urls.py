"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app_advertisements.views import index
from app_advertisements.views import home
from app_advertisements.views import top_sellers
from app_lesson_4.views import lesson_4
urlpatterns = [
    path('admin/', admin.site.urls), # http://127.0.0.1:8000/admin
    path('', home,name='home'),
    path('home/', index),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('lesson_4/', lesson_4)
]
