# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/4/24
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="myadmin_index"),
]
