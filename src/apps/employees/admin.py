from django.contrib import admin

from apps.employees import models


admin.site.register(models.Specialization)
admin.site.register(models.Position)
admin.site.register(models.Employee)
