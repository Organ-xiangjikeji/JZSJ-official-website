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
from django.conf.urls import url,include
from web import views
from web import tests
from xjkj import settings
from django.views.static import serve
urlpatterns = [
	path('admin/', admin.site.urls),
    url('staff',include('staff.urls')),
	url('^index/$', views.index, name='index'),
	url('^cases/$', views.case, name='case'),
	url('^free_data/$', views.free_data, name='free_data'),
	url('^job/$', views.job, name='job'),
	url('^about/$', views.introduce, name='about'),
	url('^map/$', views.map, name='map'),
	url('^contact/$', views.Contact.as_view(), name='contact'),
	url('^test/$', tests.test, name='test'),
	url('^api/get_vcode_img/$', views.get_vimg, name='get_vcode_img'),
   url('^api/vcode_check/$', views.Vcode.as_view(), name='vcode_check'),
	# url('^api/get_data/$', views.get_data, name='get_data'),
	# url('^$', views.get_data, name='get_data'),
	url('^data/(?P<uid>\w+)/$', views.data_detail,name='data_detail'),
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": settings.MEDIA_ROOT}),
	url(r'^register/$',views.Reg.as_view(),name='register'),
	url(r'^download/(?P<uid>\w+)/$', views.download, name='download'),

]
