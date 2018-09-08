import datetime
import random
from web.common import redis_op
from web import models
import logging

logger = logging.getLogger('django')
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

 

class MyPagenator(object):
	"""
	分页
	"""
	num = 10
	plist_len = 9
	
	def __init__(self, queryset, page):
		"""
		:param queryset:
		:param p:
		"""
		self.queryset = queryset
		self.p = page
		self.query_list, self.p_list, self.tp, self.np, self.rp = self._pg(self.queryset, self.num, self.p)
	def _pg(self, queryset, num, p):
		"""
		:param queryset:
		:param num:
		:param p: 接收到的页面参数
		:return: query_list:结果集；p_list:页面集；tp:接收到的页面参数；np:下一页；
		         rp:上一页；
		"""
		p = int(p)
		start = (p - 1) * self.num
		end = p * self.num
		querylen = queryset.count()
		if querylen / num > querylen // num:
			pcount = querylen // num + 1
		else:
			pcount = querylen // num
		if end > querylen or start < 0:
			end = querylen
			if p > pcount or p < 0:
				start = 0
				end = 0
				pcount = 0
				p = None
				self.queryset =[]
		queryset = queryset[start:end]
		p_list = [x+1 for x in range(pcount)]
		tp = p
		self.pcount = pcount
		self.tp = p
		p_list = list(filter(self._filter_pg,p_list))
		np = None
		rp = None
		blp = None
		brp = None
		try:
			if tp == p_list[-1] and tp != 1:
				np = tp
				rp = tp - 1
			elif tp == p_list[0]:
				rp = tp
				np = tp + 1
			else:
				np = tp + 1
				rp = tp - 1
		except Exception as e:
			logger.error(e)
		if tp + MyPagenator.plist_len // 2 < pcount:
			print(tp + MyPagenator.plist_len // 2 ,pcount)
			brp = tp + MyPagenator.plist_len // 2
		elif (tp - MyPagenator.plist_len // 2) > 0:
			blp = tp - MyPagenator.plist_len // 2
		else:
			pass
		self.brp = brp
		self.blp = blp
		print('nonw')
		print(tp + MyPagenator.plist_len // 2, len(p_list))
		
		return queryset,p_list, tp, np, rp
	def _filter_pg(self,p):
	
		if self.pcount-self.tp < MyPagenator.plist_len//2:
			if self.pcount - p < MyPagenator.plist_len:
				return True
		elif self.tp <= MyPagenator.plist_len//2:
			if p <= MyPagenator.plist_len:
				return True
		else:
			if abs(self.tp - p) <= MyPagenator.plist_len//2:
				return True
			 
	 


def check_vcode(request):
	ret = {'status':0}
	vkey = request.POST.get('vkey')
 
	vcode = request.POST.get('vcode')
 
	v_c = None
	try:
		v_c = redis_op.redis_conn.get(vkey).decode('utf-8')
	except Exception as e:
		logger.error(e)
		
	if v_c:
		try:
			if v_c.upper() != vcode.upper():
				ret['status'] = 1
		except Exception as e:
			logger.error(e)
			ret['status'] = 1
		return ret
	else:
		ret['status'] = 2
		return ret
def sizeConvert(size):# 单位换算
        K, M, G = 1024, 1024**2, 1024**3
        print('convert',size)
        if size >= G:
            return str(size/G)+'GB'
        elif size >= M:
            return str(size/M)+'MB'
        elif size >= K:
            return str(size/K)+'KB'
        else:
            return str(size)+'bytes'
def data_set_size(data):
	size = sizeConvert(data.file.size)
	print('hohohhhhh',size)
	if size[-2:] == 'GB':
		data.size = 3
	elif size[-2:] == 'MB':
		data.size = 2
	else:
		data.size = 1
	print('hhhh',data.size)
	return data.size
 
 
def check_pcode(request):
	ret = {
		'status':0,
		'msg':'验证成功'
	}
	return ret
def check_phone(request):
	try:
		phone = request.POST.get('phone')
		p = models.UserInfo.objects.get(phone=phone)
		if p :
		
			return False
	except Exception as e:

		logger.error(e)
	return True
def send_pcode():
	pass