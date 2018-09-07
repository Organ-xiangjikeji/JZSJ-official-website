from django.db import models
# from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
# Create your models here.
class BaseModel(models.Model):
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')
	class Meta:
		abstract = True
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

class Province(models.Model):
	name = models.CharField(verbose_name='省份',max_length=56)
	def __str__(self):
		return self.name
class Data(BaseModel):
	name = models.CharField(max_length=128, verbose_name='名称', unique=True)
	uid = models.CharField(max_length=10, verbose_name='唯一标识', unique=True, default=3)
	file = models.FileField(upload_to='datas/', verbose_name='文件地址')
	head = models.FileField(upload_to='heads/',default='heads/head1.jpg',verbose_name='文件头图')
	desc = models.CharField(max_length=512,verbose_name='数据描述',default='数据描述')
	data_source = models.ForeignKey('DataSource', verbose_name='数据来源', on_delete=models.SET_DEFAULT, default=8,
	                                blank=True)
	size_choices = ((1,'KB'),(2,'MB'),(3,'GB'))
	size = models.SmallIntegerField(choices=size_choices,verbose_name='数据规格',default=1)
	data_type = models.ForeignKey('DataType', verbose_name='数据形式', on_delete=models.SET_DEFAULT, default=4)
	industry = models.ForeignKey('Industry', verbose_name='行业类型', on_delete=models.SET_DEFAULT, default=21)
	sub_industry = models.ForeignKey('SubIndustry', verbose_name='细分行业', on_delete=models.SET_DEFAULT, default=45)
	years_choices = ((1,'古代'),(2,'近代'),(3,'现代'))
	years = models.SmallIntegerField(choices=years_choices,verbose_name='数据年份',default=3)
	upload_time = models.DateTimeField(auto_now_add=True, verbose_name='上传日期')
	status_choices = ((1, '原始数据'), (2, '标注数据'))
	province = models.ForeignKey('Province',verbose_name='省份',on_delete=models.SET_DEFAULT,default=1)
	status = models.SmallIntegerField(choices=status_choices, verbose_name='数据状态')
	pageviews = models.IntegerField(verbose_name='浏览量', default=0)
	downloads = models.IntegerField(verbose_name='下载量', default=0)
	
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = '数据资源表'
		verbose_name_plural = verbose_name
		index_together = (('name','create_time','uid'))
		


class UserInfo(models.Model):
	phone = models.CharField(max_length=11,unique=True)
	def __str__(self):
		return self.phone
	
	class Meta:
		verbose_name = '用户表'
		verbose_name_plural = verbose_name
class UserBehavior(models.Model):
	user = models.ForeignKey('UserInfo',verbose_name='用户名',on_delete=models.SET_DEFAULT,default=1)
	industry = models.ForeignKey('Industry',verbose_name='浏览行业',default=21,on_delete=models.SET_DEFAULT)
	times = models.IntegerField(verbose_name='浏览次数',default=0)
	
	
class Customer(models.Model):
	user = models.CharField(max_length=56,verbose_name='姓名')
	email = models.EmailField(
		verbose_name='邮箱地址',
		max_length=128,
		unique=True,
		null=True)
	corp = models.CharField(max_length=64,verbose_name='公司名',null=True,blank=True)
	phone = models.CharField(max_length=11, unique=True,verbose_name='手机号')
	needs = models.TextField(max_length=3072,verbose_name='需求',null=True,blank=True)
	memo = models.TextField(max_length=5120,verbose_name='备注',default='备注',null=True,blank=True)
	
	def __str__(self):
		return self.user

	
	
