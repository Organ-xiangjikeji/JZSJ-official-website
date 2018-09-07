from django.shortcuts import render, HttpResponse, redirect
from web import models
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from web.common import utils
from web.common.orm_op import Myquery
from web.common import vcode
from web.common.redis_op import redis_conn
from django.views.generic import View
from web.common import myform
from web.common.decroters import urecord
import logging

logger = logging.getLogger('django')
# Create your views here.
from web.common import utils
# @cache_page(60*2)
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

	data_set = models.Data.objects.all()
	myquery = Myquery(request)
	pg = None
	print('first filter',myquery.nquery_set.count())
	if myquery.nquery_set.count() != 0:
		try:
			page =  request.GET.get('page', '1')
			if page.isdigit():
				pg = utils.MyPagenator(myquery.nquery_set, page)
			else:
				return render(request,'404page.html',{'msg':'您的请求错误'})
		except Exception as e:
			logger.error(e)
	
	response = render(request, 'free_data.html', {
	                                          'myquery': myquery,
	                                          'pg': pg})
	# response.delete_cookie('filters')
	response.set_cookie('filters',myquery.filters)
	return response


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


class Contact(View):
	def get(self, request):
		return render(request, "contact.html")
	
	def post(self, request):
		ret = {
			'status': 0,
			'msg': 'success'
		}
		if  not request.is_ajax():
			ret = {'status':1,'msg':'请求错误'}
			return JsonResponse(ret)
		v_check = utils.check_vcode(request)
		if v_check['status'] == 1:
			ret['status'] = 1
			ret['msg'] = '验证码错误'
			return JsonResponse(ret)
		elif v_check['status'] == 2 :
			ret['status'] = 1
			ret['msg'] = '验证码已过期'
			return JsonResponse(ret)
		
		form = myform.CustomerForm(request.POST)
		try:
			if form.is_valid():
				form.save()
			else:
				ret['status'] = 1
				print(form.errors)
				ret['msg'] = '数据提交失败，您的手机或邮箱信息可能已经提交'
		
		except Exception as e:
			logger.error(e)
			ret['status'] = 1
			ret['msg'] = '数据提交失败'
		return JsonResponse(ret)


def get_vimg(request):
	"""
	获取验证码
	:param request:
	:return:
	"""
	
	text, image = vcode.gen_captcha_text_and_image()
	v_key = request.GET.get('vk')
	ex_key = request.GET.get('ex')
	if ex_key:
		try:
			redis_conn.delete(ex_key)
		except Exception as e:
			logger.error(e)
	
	redis_conn.set(v_key, text, 60*3)
	
	return HttpResponse(image.getvalue(), content_type='image/jpg')


@urecord
def data_detail(request, uid):
	data = models.Data.objects.get(uid=uid)
	
	return render(request, 'data_detail.html', {'data': data})


class Reg(View):
	def get(self, request):
		

		return render(request, 'register.html')
	
	def post(self, request):
		ret = {
			'status': 0,
			'msg': 'success'
		}
		if not request.is_ajax():
			ret = {'status': 1, 'msg': '请求错误'}
			return JsonResponse(ret)
		pcode_check = utils.check_pcode(request)
		if pcode_check['status'] == 1: #验证手机验证码
			ret['status'] = 1
			ret['msg'] = '手机验证码错误'
			return JsonResponse(ret)
		try:
			user = models.UserInfo.objects.get_or_create(phone=request.POST.get('phone'))
			request.session['user'] = user[0].phone
			request.session['is_login'] = True
			request.session.set_expiry(60 * 60 * 12)
		except Exception as e:
			logger.error(e)
			ret['status'] = 1
			ret['msg'] = '此号已注册'
 
		return JsonResponse(ret)
class Vcode(View):
	def post(self, request):
		ret = {
			'status': 0,
			'msg': 'success'
		}
		if not request.is_ajax():
			ret = {'status': 1, 'msg': '请求错误'}
			return JsonResponse(ret)
		v_check = utils.check_vcode(request)
		
		if v_check['status'] == 2:
			ret['status'] = 1
			ret['msg'] = '验证码已过期'
			return JsonResponse(ret)
		elif v_check['status'] == 1:
			ret['status'] = 1
			ret['msg'] = '验证码错误'
			return JsonResponse(ret)
		print('hhhhhhhh')
		if not utils.check_phone(request):
			ret['status'] = 1
			ret['msg'] = '手机号码已注册'
		utils.send_pcode()
		return JsonResponse(ret)
 
from django.http import FileResponse




def download(request,uid):
	data =  models.Data.objects.get(uid=uid)
	data.downloads += 1
	data.save()
	file = open(data.file.path, 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="%s"'%file.name
	return response
	
