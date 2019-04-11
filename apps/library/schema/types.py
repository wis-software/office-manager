import graphene

from graphene_django.types import DjangoObjectType

from apps.library import models


class BookType(DjangoObjectType):
    is_available = graphene.Boolean()

    def resolve_is_available(self, info):
        return not self.holder_history.filter(refunded_at=None).exists()

    class Meta:
        model = models.Book
        filter_fields = {
            'name': ['icontains', 'istartswith'],
            'description': ['icontains', 'istartswith'],
            'authors': ['in'],
            'tags': ['in'],
            'specializations': ['icontains', 'istartswith'],
            'id': ['exact']
        }


class BookHolderType(DjangoObjectType):
    class Meta:
        model = models.Holder
        filter_fields = {
            'id': ['exact'],
            'book': ['exact'],
            'employee': ['exact'],
            'refunded_at': ['exact', 'date', 'gte', 'lte', 'lt', 'gt',
                            'isnull'],
            'created_at': ['exact', 'date', 'gte', 'lte', 'lt', 'gt']
        }


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact'],
        }


class BookOfferType(DjangoObjectType):
    class Meta:
        model = models.Offer
        filter_fields = {
            'description': ['exact', 'icontains'],
            'id': ['exact']
        }
