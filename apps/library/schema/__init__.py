import graphene
from graphene_django.types import ObjectType
from graphene_django_extras import DjangoFilterPaginateListField

from apps.library.schema import mutation
from apps.library.schema import types
from apps.library import models

__all__ = [
    'LibraryQuery', 'LibraryMutation'
]


class LibraryQuery(ObjectType):
    """
    Library Query type for GraphQL.
    """

    books = DjangoFilterPaginateListField(types.BookType)
    holders = DjangoFilterPaginateListField(types.BookHolderType)
    offers = DjangoFilterPaginateListField(types.BookOfferType)
    tags = DjangoFilterPaginateListField(types.TagType)

    total_books = graphene.Int()
    total_tags = graphene.Int()
    total_offers = graphene.Int()
    total_holders = graphene.Int()

    @staticmethod
    def resolve_total_books():
        return models.Book.objects.all().count()

    @staticmethod
    def resolve_total_tags():
        return models.Tag.objects.all().count()

    @staticmethod
    def resolve_total_offers():
        return models.Offer.objects.all().count()

    @staticmethod
    def resolve_total_holders():
        return models.Holder.objects.all().count()

    class Meta:
        abstract = True


class LibraryMutation(ObjectType):
    """
    Library Mutation type.
    """

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
