from django.contrib import admin

from apps.library import models


admin.site.register(models.Book)
admin.site.register(models.Holder)
admin.site.register(models.Offer)
admin.site.register(models.Tag)
