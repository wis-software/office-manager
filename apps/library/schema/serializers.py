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


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class BookPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'
