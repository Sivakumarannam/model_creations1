"""
URL configuration for model_creations1 project.

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topics/',display_topics,name='display_topics'),
    path('display_webpages/',display_webpages,name='display_webpages'),
    path('display_access_records/',display_access_records,name='display_access_records'),
    path('display_players/',display_players,name='display_players'),
    path('insert_topics/',insert_topics,name='insert_topics'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_access_records/',insert_access_records,name='insert_access_records'),
    path('insert_players/',insert_players,name='insert_players'),
]
