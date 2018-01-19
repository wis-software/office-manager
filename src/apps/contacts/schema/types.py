from graphene_django.types import DjangoObjectType

from apps.contacts import models


class EmailType(DjangoObjectType):
    class Meta:
        model = models.Email
        filter_fields = {
            'email': ['iexact'],
            'is_active': ['exact']
        }


class PhoneNumberType(DjangoObjectType):
    class Meta:
        model = models.PhoneNumber
        filter_fields = {
            'id': ['exact'],
            'number': ['exact', 'icontains'],
            'is_active': ['exact']
        }


class SkypeType(DjangoObjectType):
    class Meta:
        model = models.Skype
        filter_fields = {
            'id': ['exact'],
            'login': ['exact', 'icontains'],
            'is_active': ['exact']
        }


class GitAccountType(DjangoObjectType):
    class Meta:
        model = models.GitAccount
        filter_fields = {
            'id': ['exact'],
            'url': ['icontains'],
            'account': ['exact', 'icontains'],
            'is_active': ['exact']
        }
