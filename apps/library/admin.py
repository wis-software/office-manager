from django.contrib import admin

from apps.library import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description', 'tag__name')


@admin.register(models.Holder)
class HolderAdmin(admin.ModelAdmin):
    search_fields = ('employee__first_name', 'book__name')


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'about')


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
