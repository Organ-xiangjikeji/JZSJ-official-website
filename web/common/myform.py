from django.forms import ModelForm
from django.core.exceptions import ValidationError
from web import models
import re


def creat_model_form(model):
	print(model)
	
	class Meta:
		model = models.Customer
		fields = "__all__"
	
	def default_clean(self):
		error_list = []
		self.ValidationError = ValidationError
		if self.errors:
			for error, m in list(self.errors.items()):
				if m.as_text() == '* This field is required.':
					self.errors.pop(error)
		
		if error_list:
			raise ValidationError(error_list)
	
	def __new__(cls, *args, **kwargs):
		for field_name, field_obj in cls.base_fields.items():
			field_obj.widget.attrs.update({'class': 'form-control'})
			if type(field_obj).__name__ in ['DateField', 'DateTimeField']:
				if not getattr(model._meta.get_field(field_name), 'auto_now_add', None):
					field_obj.widget.input_type = 'date'
		
		return ModelForm.__new__(cls)
	
	_model_form_class = type("DynamicModelForm", (ModelForm,), {'Meta': Meta})
	
	setattr(_model_form_class, '__new__', __new__)
	setattr(_model_form_class, 'clean', default_clean)
	
	return _model_form_class


class CustomerForm(ModelForm):
	class Meta:
		model = models.Customer
		fields = "__all__"
	
	def clean_phone(self):
		phone = self.cleaned_data['phone']
		phone_regex = r'^1[345789]\d{9}$'
		p = re.compile(phone_regex)
		if p.match(phone):
			return phone
		else:
			raise ValidationError('手机号码非法', code='invalid mobile')
	 
		
