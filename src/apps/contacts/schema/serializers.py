from rest_framework import serializers

from apps.contacts import models


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = '__all__'


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = '__all__'


class SkypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skype
        fields = '__all__'


class GitAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GitAccount
        fields = '__all__'
