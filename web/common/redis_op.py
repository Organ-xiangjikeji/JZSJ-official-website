import redis

from xjkj import settings
from django_redis import get_redis_connection


class IpConn(object):
	__instance = None
	
	def __init__(self):
		self._conn = redis.Redis(host=settings.REDIS_ADDR, port=settings.REDIS_PORT, db=3)
	
	def __new__(cls, *args, **kwargs):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls, *args, **kwargs)
		return cls.__instance
	
redis_conn = get_redis_connection('vcode')

user_conn = get_redis_connection('user')

ip_conn = IpConn()
