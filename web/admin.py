from django.contrib import admin
from web import models
# Register your models here.
admin.site.register(models.Industry)
admin.site.register(models.DataType)
admin.site.register(models.Data)
admin.site.register(models.DataSource)
admin.site.register(models.SubIndustry)

