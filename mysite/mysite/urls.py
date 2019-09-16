"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin

from firstproject.views import list_items,create_item,update_item,delete_item,home_view
#from firstproject.views import home_view

urlpatterns = [

    path('home/', home_view ,name='home_view'),
    path('list/', list_items , name='list_items'),
    path('create/',create_item,name='create_items'),
    path('update/<int:id>/',update_item,name='update_item'),
    path('delete/<int:id>/',delete_item,name='delete_item'),
    path('admin/', admin.site.urls)


]
