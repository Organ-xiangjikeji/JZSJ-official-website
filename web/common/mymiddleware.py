from django.utils.deprecation import MiddlewareMixin
from web.common.redis_op import ip_conn
from django.shortcuts import render, HttpResponse, redirect
import time
print(time.time())
class Throttle(MiddlewareMixin):
	
	def process_request(self, request):
		print('request')
		ip = None
		count = None
		if request.META.get('HTTP_X_FORWARDED_FOR'):
			ip = request.META['HTTP_X_FORWARDED_FOR']
		else:
			ip = request.META['REMOTE_ADDR']
	
		now_time = time.time()
		ip_conn._conn.rpush(ip,now_time)
		for i in ip_conn._conn.lrange(ip, 0, -1):
			ex_time = float(i)
			interval = now_time - ex_time
			if interval > 60:
				ip_conn._conn.lpop(ip)
		m = ip_conn._conn.llen(ip)
		print(m)
		if m != 0:
			if m >60 and interval<61:
				return HttpResponse('您的访问频率过快,请1分钟后再试')
		
 
		
	
	def process_response(self, request, response):
		
	 
		return response
