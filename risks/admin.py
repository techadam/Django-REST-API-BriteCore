from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RiskType)
admin.site.register(models.RiskField)
admin.site.register(models.FieldType)