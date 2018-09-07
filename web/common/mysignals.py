# from django.db.models.signals import pre_save, post_save
# from web.common.utils import sizeConvert
# from web import models
#
# def pre_save_func(sender, **kwargs):
# 	print("pre_save_func")
# 	print("pre_save_msg:", sender, kwargs)
#
#
# def post_save_func(sender, instance, **kwargs):
# 	print("post_save_func")
# 	# print(instance.file)
# 	print(instance.id)
# 	data = models.Data.objects.get(id=instance.id)
# 	print(data.file.url)
#
# 	print(dir(instance))
#
# 	print("post_save_msg:", sender, kwargs)
#
#
# pre_save.connect(pre_save_func)  # models对象保存前触发callback函数
# post_save.connect(post_save_func)
