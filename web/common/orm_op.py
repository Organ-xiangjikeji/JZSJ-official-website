from web import models
import logging
from django.db.models import Q
logger = logging.getLogger('django')

class Myquery(object):
	def __init__(self,request):
		self.request = request
		self.filters = []
		self.query_set = self._get_raw_data()
		self.industry, self.source,self.type, self.sub_industry,self.status,self.dys,self.province,self.size,self.nquery_set = self._get_data_set(self.query_set,self.request)
		self.data_sources,self.data_types,self.data_status,self.industrys,self.years,self.provinces,self.sizes = self._get_options()
		self.ranking_list = self._get_data_ranking()
	def _get_raw_data(self):
		return models.Data.objects.all()
	
	def _get_data_set(self,query_set, request):
		"""
		筛选
		:param query_set:
		:param request:
		:return:
		"""
		industry = None
		source = None
		type = None
		sub_industry = None
		dys = 0
		province = None
		
		size = 0

		status = 0
		
		request.session.set_expiry(0)
		self.filters.append({'sub_industry', 1})
		self.filters.append({'size',2})
		
 
	 
		
		industry_uid = request.GET.get('industry', '0')
		if industry_uid and industry_uid != '0':
			try:
				industry = models.Industry.objects.get(uid=industry_uid)
				query_set = query_set.filter(industry__uid=industry_uid)
			except Exception as e:
				logger.error(e)
		if request.GET.get('sub_industry',None):
			sub_industry_id = 0
			try:
				sub_industry_id = int(request.GET.get('sub_industry', 0))
			except Exception as e:
				logger.error(e)
			if sub_industry_id != 0:
				sub_industry = models.SubIndustry.objects.get(id=sub_industry_id)
				query_set = query_set.filter(sub_industry_id=sub_industry_id)
			 
		if request.GET.get('source',None):
			source_id = 0
			try:
				source_id = int(request.GET.get('source', 0))
			except Exception as e:
				logger.error(e)
				
			if source_id != 0:
				try:
					source = models.DataSource.objects.get(id=source_id)
					query_set = query_set.filter(data_source_id=source_id)
				except Exception as e:
					logger.error(e)
		
		if request.GET.get('type',None):
			type_id = 0
			try:
				type_id = int(request.GET.get('type', 0))
			except Exception as e:
				logger.error(e)
			if type_id != 0:
				try:
					type = models.DataType.objects.get(id=type_id)
					query_set = query_set.filter(data_type_id=type_id)
				except Exception as e:
					logger.error(e)
		if request.GET.get('status',None):
			try:
				status = int(request.GET.get('status'))
				self.status_text = models.Data.status_choices[status-1][1]
			except Exception as e:
				logger.error(e)
			if status != 0:
				try:
					query_set = query_set.filter(status=status)
				except Exception as e:
					logger.error(e)
		if request.GET.get('size',None):
			try:
				size = int(request.GET.get('size'))
				print('size',size)
				self.size_text = models.Data.size_choices[size-1][1]
			except Exception as e:
				logger.error(e)
			if size != 0:
				try:
					query_set = query_set.filter(size=size)
				except Exception as e:
					logger.error(e)
		if request.GET.get('dys',None):
			try:
				dys = int(request.GET.get('dys',None))
				self.dys_text = models.Data.years_choices[dys-1][1]
			except Exception as e:
				logger.error(e)
			if dys != 0:
				try:
					query_set = query_set.filter(years=dys)
				except Exception as e:
					logger.error(e)
		if request.GET.get('province',None):
			province_id = 0
			try:
				province_id = int(request.GET.get('province'))
			except Exception as e:
				logger.error(e)
			if province_id != 0:
				try:
					province = models.Province.objects.get(id=province_id)
					query_set = query_set.filter(province_id=province_id)
				except Exception as e:
					logger.error(e)
		

		 
				
		return industry, source, type,sub_industry,status,dys,province,size,query_set
	
	def _get_options(self):
		data_sources = []
		try:
			data_sources = models.DataSource.objects.all().order_by('ordernum')
		except Exception as e:
			logger.error(e)
		data_types =[]
		try:
			data_types = models.DataType.objects.all().order_by('ordernum')
		except Exception as e:
			logger.error(e)
		years = [list(x) for x in models.Data.years_choices]
		data_status = models.Data.status_choices
		industrys = []
		sizes = models.Data.size_choices
		try:
			industrys = models.Industry.objects.all().exclude(id=21).order_by('ordernum')
		except Exception as e:
			logger.error(e)
		
		provinces = []
		try:
			provinces = models.Province.objects.all()
		except Exception as e:
			logger.error(e)
 
	
		return data_sources, data_types, data_status, industrys,years,provinces,sizes
	def _get_data_ranking(self):
		try:
			data_set_ranking = models.Data.objects.order_by('-downloads')[:10]
		except Exception as e:
			logger.error(e)

		return data_set_ranking
	
	
	
