import graphene
from graphene_django.types import ObjectType
from graphene_django_extras import DjangoFilterPaginateListField
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination

from apps.library import models
from apps.library.schema import mutation
from apps.library.schema import types

__all__ = [
    'BooksQuery', 'BooksMutation'
]


class BooksQuery(ObjectType):
    books = DjangoFilterPaginateListField(types.BookType)
    holders = DjangoFilterPaginateListField(types.BookHolderType)
    offers = DjangoFilterPaginateListField(types.BookOfferType)
    tags = DjangoFilterPaginateListField(types.TagType)
    total_books = graphene.Int()

    class Meta:
        abstract = True

    def resolve_total_books(self, *args, **kwargs):
        return models.Book.objects.all().count()

    def resolve_books(self, info):
        return models.Book.objects.all()

    def resolve_holders(self, info):
        return models.Holder.objects.all()

    def resolve_offers(self, info):
        return models.Offer.objects.all()

    def resolve_tags(self, info):
        return models.Tag.objects.all()


class BooksMutation(ObjectType):
    tag_create = mutation.ModelTagMutation.CreateField()
    tag_update = mutation.ModelTagMutation.UpdateField()
    tag_delete = mutation.ModelTagMutation.DeleteField()

    book_create = mutation.ModelBookMutation.CreateField()
    book_update = mutation.ModelBookMutation.UpdateField()
    book_delete = mutation.ModelBookMutation.DeleteField()

    holder_create = mutation.ModelBookHolderMutation.CreateField()
    holder_update = mutation.ModelBookHolderMutation.UpdateField()
    holder_delete = mutation.ModelBookHolderMutation.DeleteField()

    offer_create = mutation.ModelOfferMutation.CreateField()
    offer_update = mutation.ModelOfferMutation.UpdateField()
    offer_delete = mutation.ModelOfferMutation.DeleteField()

    class Meta:
        abstract = True

