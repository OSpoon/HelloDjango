"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from application import views

urlpatterns = [
    # 正则匹配
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^article/2017/', views.article),
    # 加括号分组参数
    url(r'^articles/([0-9]{4})/$', views.articles1),
    # 加括号分组多个参数
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.articles2),
    # 加括号分组多个参数指定匹配参数名s
    url(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<d>[0-9]{2})/$', views.articles3),
    # 参数名称一致,正则匹配参数跟v3内的参数名称重复,参数值会被v3中的值覆盖
    url(r'^articles/', views.articles4, {'yyyy': '2017', 'mm': '10', 'dd': '21'}),
    url(r'^login/', views.login, {'arg': '2017'}, name='alex'),
]
