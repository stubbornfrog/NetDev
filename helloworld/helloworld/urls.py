# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/4/24
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('myadmin/', include('myadmin.urls')),
    path('', include('myhome.urls')),
]
