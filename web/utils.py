import datetime
import time
import random
from web import models


# 10进制转换36进制
def hex36(num):
	key = '1qaz2wssxcde34rfvbgt56yhnmju78iklo9p0'
	a = []
	while num != 0:
		n = num % 6
		
		a.append(key[n])
		num = num // 36
	a.reverse()
	out = ''.join(a)
	return out


# 获取唯一标识
def getId():
	d1 = datetime.datetime(2018, 9, 1)
	d2 = datetime.datetime.now()
	s = (d2 - d1).days * 24 * 60 * 60
	ms = d2.microsecond
	id1 = hex36(random.randint(36, 1295))
	id2 = hex36(s)
	id3 = hex36(ms + 46656)
	
	mId = id1 + id2 + id3
	
	return mId[::-1]


def get_data_set(query_set, request):
	"""
	筛选
	:param query_set:
	:param request:
	:return:
	"""
	print(request.GET)
	industry = None
	source = None
	type = None
	industry_uid = request.GET.get('industry', '0')
	print('hehe', industry_uid)
	if industry_uid and industry_uid != '0':
		print(industry_uid)
		industry = models.Industry.objects.get(uid=industry_uid)
		query_set = query_set.filter(industry__uid=industry_uid)
	
	if request.GET.get('source'):
		source_id = int(request.GET.get('source', 0))
		if source_id != 0:
			source = models.DataSource.objects.get(id=source_id)
			query_set = query_set.filter(data_source_id=source_id)
	if request.GET.get('type'):
		type_id = int(request.GET.get('type', 0))
		if type_id != 0:
			type = models.DataType.objects.get(id=type_id)
			query_set = query_set.filter(data_type_id=type_id)
	
	return industry, source, type, query_set


def paginate(request, query_set):
	"""
	分页
	:param request:
	:param query_set:
	:return:
	"""
	pass
