from web.common.redis_op import user_conn
from web import models
from web.common.log import logger

def get_urecord():
	users = user_conn.keys()
	for name in users:
		name = name.decode('utf-8')
		keys = user_conn.hkeys(name)
		industry_id = None
		times = 0
		user = None
		userbehavior = None
		try:
			user = models.UserInfo.objects.get(phone=name)
		except Exception as e:
			logger.error(e)
		
		for k in keys:
			try:
				industry_id = int(k)
			except Exception as e:
				logger.error(e)
			try:
				times = int(user_conn.hget(name,k))
			except Exception as e:
				logger.error(e)
			try:
				userbehavior = models.UserBehavior.objects.get(user=user, industry_id=industry_id)
			except Exception as e:
				logger.error(e)
			if userbehavior:
				userbehavior.times += times
				userbehavior.save()
				user_conn.delete(name)
			else:
				try:
					models.UserBehavior.objects.create(user=user,industry_id=industry_id,times=times)
					user_conn.delete(name)
				except Exception as e:
					
					logger.error(e)
		
 