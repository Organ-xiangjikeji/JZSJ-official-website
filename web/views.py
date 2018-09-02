from django.shortcuts import render, HttpResponse
from web import models


# Create your views here.
def index(request):
	"""首页"""
	return render(request, 'index.html')


def case(request):
	"""案例与服务"""
	return render(request, 'case.html')


def free_data(request):
	"""
	数据下载页
	:param request:
	:return:
	"""
	data_sources = models.DataSource.objects.all().order_by('ordernum')
	data_types = models.DataType.objects.all().order_by('ordernum')
	data_status = models.Data.status_choices
	from web.utils import getId
	industrys = models.Industry.objects.all().order_by('ordernum')
	data_set = models.Data.objects.all()
	from web.utils import get_data_set
	industry, source, type, data_set = get_data_set(data_set, request)
	print(dir(data_set))
	import random
	import datetime
	
	data_set_ranking = models.Data.objects.order_by('-downloads')[:10]
	
	return render(request, 'free_data.html', {'data_souces': data_sources,
	                                          'data_types': data_types,
	                                          'data_status': data_status,
	                                          'industrys': industrys,
	                                          'data_set': data_set,
	                                          'industry': industry,
	                                          'source': source,
	                                          'type': type,
	                                          'data_set_ranking': data_set_ranking})


def job(request):
	"""工作机会"""
	return render(request, 'job.html')


def introduce(request):
	"""
	关于我们
	:param request:
	:return:
	"""
	return render(request, 'introduce.html')


def map(request):
	"""
	获取百度地图
	:param request:
	:return:
	"""
	return render(request, "map.html")


def contact(request):
	"""
	获取客户联系信息
	:param request:
	:return:
	"""
	return render(request, "contact.html")


def get_vimg(request):
	"""
	获取验证码
	:param request:
	:return:
	"""
	from web import vcode
	text, image = vcode.gen_captcha_text_and_image()
	
	return HttpResponse(image.getvalue(), content_type='image/jpg')


def get_data(request):
	contact()
	return HttpResponse('hello')
