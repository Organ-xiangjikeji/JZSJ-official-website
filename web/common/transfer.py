from web.common import redis_op
from web import models
from web.common.log import logger


def get_urecord():
	users = redis_op.redis_conn._conn.keys()
	for name in users:
		print(name)
		keys = redis_op.redis_conn._conn.hkeys(name)
		for k in keys:
			try:
				industry_id = int(redis_op.redis_conn._conn.hget(name, k))
			except Exception as e:
				logger.error(e)
			try:
				times = redis_op.redis_conn._conn.hget(name, k)
			except Exception as e:
				logger.error(e)
		user = None
		try:
			user = models.UserBehavior.objects.get(user=name, industry_id=industry_id)
		except Exception as e:
			logger.error(e)
		if user:
			user.times += times
			user.save()
		else:
			try:
				models.UserBehavior.objects.create(user=name, industry_id=industry_id, times=times)
			except Exception as e:
				logger.error(e)

