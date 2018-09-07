from django.db.models.signals import pre_save, post_save



def pre_save_func(sender, **kwargs):
	print("pre_save_func")
	print("pre_save_msg:", sender, kwargs)


def post_save_func(sender, instance, created, **kwargs):
	
	print("post_save_func")
	# if created:
	# 	print(instance.id)
	# 	from web.common.utils import data_set_size,sizeConvert
	# 	from web import models
	# 	data = models.Data.objects.get(id=instance.id)
	# 	data.size
	# 	data_set_size(data)
	# 	print('created',data.size)
	#
	
	print("post_save_msg:", sender, kwargs)


# pre_save.connect(pre_save_func)  # models对象保存前触发callback函数
# post_save.connect(post_save_func)
