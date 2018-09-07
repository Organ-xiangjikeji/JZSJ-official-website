from django.shortcuts import   redirect
from web import models
from web.common.redis_op import user_conn
from web.common.log import logger

def urecord(func):
	def inner(request, uid):
		print(dir(request.session))
		print('hello',request.session.has_key('user'))
		print(request.session.has_key('is_logint'))
		if not request.session.has_key('is_login'):
			return redirect('/register?next=/data/' + uid)
		data = None
		user_phone = None
		try:
			user_phone = request.session['user']
		except Exception as e:
			logger.error(e)
		
		try:
			data = models.Data.objects.get(uid=uid)
		except Exception as e:
			logger.error(e)
		if data:
			data.pageviews += 1
			data.save()
			industry_id = data.industry.id
			count = None
		try:
			count = int(user_conn.hget(user_phone, industry_id))
		except Exception as e:
			logger.error(e)
		if not count:
			count = 1
		else:
			count = int(count) + 1
		try:
			user_conn.hset(user_phone, industry_id, count)
		except Exception as e:
			logger.error(e)
		result = func(request, uid)
		return result
	
	return inner