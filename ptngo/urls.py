"""ptngo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app import views as app_views  # new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', app_views.index, name='index'),
	url(r'^index/$', app_views.index, name='index'),
    url(r'^login/$', app_views.dellogin), 
    url(r'^logout/$', app_views.logout), 
    url(r'^regist/$', app_views.delregist),
    url(r'^map/(\S+)/(\S+)/$', app_views.delmap,name='delmap'), 
    url(r'^postmap/$', app_views.postmap), 
    url(r'^error/$', app_views.error,name='error'), 
    url(r'^sendmsg/$', app_views.sendmsg,name='sendmsg'), 
    url(r'^detail/$', app_views.detail,name='detail'), 
    url(r'^detail_other/(\S+)/(\S+)/(\S+)/$', app_views.detail_other,name='detail_other'), 

]
