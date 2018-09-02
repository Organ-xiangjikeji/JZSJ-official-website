"""xjkj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from web import views
from web import tests

urlpatterns = [
	path('admin/', admin.site.urls),
	url('^index/$', views.index, name='index'),
	url('^cases/$', views.case, name='case'),
	url('^free_data/$', views.free_data, name='free_data'),
	url('^job/$', views.job, name='job'),
	url('^about/$', views.introduce, name='about'),
	url('^map/$', views.map, name='map'),
	url('^contact/$', views.contact, name='contact'),
	url('^test/$', tests.test, name='test'),
	url('^api/get_img/$', views.get_vimg, name='get_img_code'),
	url('^api/get_data/$', views.get_data, name='get_data')

]
