from graphene_django_extras import DjangoSerializerMutation
from rest_framework import serializers

from apps.library import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class BookHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holder
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Offer
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = '__all__'


class ModelBookMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class ModelOfferMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = OfferSerializer


class ModelBookHolderMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = BookHolderSerializer


class ModelTagMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = TagSerializer
