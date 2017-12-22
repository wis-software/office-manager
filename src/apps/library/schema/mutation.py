from graphene_django_extras import DjangoSerializerMutation

from apps.library.schema import serializers as app_serializer


class ModelBookMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializer.BookSerializer


class ModelOfferMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializer.OfferSerializer


class ModelBookHolderMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializer.BookHolderSerializer


class ModelTagMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializer.TagSerializer
