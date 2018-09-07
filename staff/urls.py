from django.conf.urls import url
from staff import views
urlpatterns = [
	url(r'index',views.index,name='index'),]