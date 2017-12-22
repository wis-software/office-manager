import graphene

from graphene_django.types import DjangoObjectType
from graphene_django_extras import DjangoFilterPaginateListField
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination
from apps.library import models


class BaseBookHolderType(DjangoObjectType):
    """
    Position graphQL type.
    Implemented total_employees and employees objects.
    """

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


class BookType(DjangoObjectType):
    holders = DjangoFilterPaginateListField(BaseBookHolderType)
    is_available = graphene.Boolean()

    def resolve_is_available(self, info):
        return self.refunded_at is None

    class Meta:
        model = models.Book
        filter_fields = {
            'name': ['icontains', 'istartswith'],
            'description': ['icontains', 'istartswith'],
            'author': ['icontains', 'istartswith'],
            'tags': ['in'],
            'specializations': ['icontains', 'istartswith'],
            'id': ['exact']
        }


class BookHolderType(BaseBookHolderType):
    """
    Position graphQL type.
    Implemented total_employees and employees objects.
    """
    book = DjangoFilterPaginateListField(BookType)

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
    books = DjangoFilterPaginateListField(BookType)

    def resolve_books(self, info):
        return self.books.all()

    class Meta:
        model = models.Tag
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact'],
        }


class BookOfferType(DjangoObjectType):
    books = DjangoFilterPaginateListField(BookType)

    def resolve_books(self, info):
        return self.books.all()

    class Meta:
        model = models.Offer
        filter_fields = {
            'description': ['exact', 'icontains'],
            'id': ['exact']
        }
