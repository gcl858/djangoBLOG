"""
URL configuration for djangoBLOG project.

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
from posts.views import index, index_use_template, showPost,index_use_template1,showPost1,login

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('template/', index_use_template),
    path("post/<slug:slug>/", showPost),
    path('template1/', index_use_template1),
    path("post1/<slug:slug>/", showPost1),
    path("login",login)
]
