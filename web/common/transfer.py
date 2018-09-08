from web.common import redis_op
from web import models
import logging
logger = logging.getLogger('django')
def get_urecord():
	"""
	把用户访问记录存到数据库
	:return:
	"""
	users = redis_op.redis_conn.keys()
	for name in users:
		keys = redis_op.redis_conn.hkeys(name)
		user = None
		for k in keys:
			industry_id = None
			try:
				user = models.UserBehavior.objects.get(user=name, industry_id=industry_id)
			except Exception as e:
				logger.error(e)
			try:
				industry_id = int(redis_op.redis_conn.hget(name, k))
			except Exception as e:
				logger.error(e)
			times = None
			try:
				times = redis_op.redis_conn.hget(name, k)
			except Exception as e:
				logger.error(e)
			
			if user and times :
				user.times += times
				user.save()
			else:
				try:
					models.UserBehavior.objects.create(user=name, industry_id=industry_id, times=times)
				except Exception as e:
					logger.error(e)

