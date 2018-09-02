from django.db import models


# Create your models here.
class Industry(models.Model):
	name = models.CharField(max_length=128, verbose_name='名称', unique=True)
	uid = models.CharField(max_length=10, verbose_name='唯一标识', unique=True)
	ordernum = models.SmallIntegerField(verbose_name='序号', default=1)
	
	def __str__(self):
		return self.name


class DataType(models.Model):
	name = models.CharField(max_length=32, verbose_name='名称', unique=True)
	ordernum = models.SmallIntegerField(verbose_name='序号', default=1)
	
	def __str__(self):
		return self.name


class DataSource(models.Model):
	name = models.CharField(max_length=128, verbose_name='名称', unique=True)
	ordernum = models.SmallIntegerField(verbose_name='序号', default=1)
	
	def __str__(self):
		return self.name


class SubIndustry(models.Model):
	name = models.CharField(verbose_name='名称', max_length=128, unique=True)
	Industry = models.ForeignKey('Industry', verbose_name='行业', on_delete=models.CASCADE)
	ordernum = models.SmallIntegerField(verbose_name='序号', default=1)
	
	def __str__(self):
		return self.name


class Data(models.Model):
	name = models.CharField(max_length=128, verbose_name='名称', unique=True)
	uid = models.CharField(max_length=10, verbose_name='唯一标识', unique=True, default=3)
	file = models.FileField(upload_to="datas/", verbose_name='文件地址', null=True, blank=True)
	data_source = models.ForeignKey('DataSource', verbose_name='数据来源', on_delete=models.SET_NULL, null=True, default=0,
	                                blank=True)
	data_type = models.ForeignKey('DataType', verbose_name='数据形式', on_delete=models.SET_NULL, null=True, blank=True)
	industry = models.ForeignKey('Industry', verbose_name='行业类型', on_delete=models.SET_NULL, null=True, default=0,
	                             blank=True)
	sub_industry = models.ForeignKey('SubIndustry', verbose_name='细分行业', on_delete=models.SET_NULL, default=0,
	                                 null=True)
	date = models.DateTimeField(verbose_name='数据年份')
	upload_time = models.DateTimeField(auto_now_add=True, verbose_name='上传日期')
	status_choices = ((1, '原始数据'), (2, '标注数据'))
	status = models.SmallIntegerField(choices=status_choices, verbose_name='数据状态')
	pageviews = models.IntegerField(verbose_name='浏览量', default=0)
	downloads = models.IntegerField(verbose_name="下载量", default=0)
	
	def __str__(self):
		return self.name
