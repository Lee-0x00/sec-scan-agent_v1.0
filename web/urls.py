#!/usr/bin/env python
#coding:utf-8
#__author__:Bing
#email:amazing_bing@outlook.com

from django.conf.urls import include, url
from pentest.user import home
from pentest import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.login,name="login"),
    url(r'^register/',views.register,name='register'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^index/',home.user_index,name='index'),
    url(r'', include('pentest.urls')),
    #url(r'', include('scan.urls')),
    #url(r'', include('admin.urls')),
    #url(r'', include('report.urls')),
]
