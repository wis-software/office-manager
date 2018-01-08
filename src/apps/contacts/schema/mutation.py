from graphene_django_extras import DjangoSerializerMutation

from apps.contacts.schema import serializers as app_serializers


class ModelEmailMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.EmailSerializer


class ModelPhoneNumberMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.PhoneNumberSerializer


class ModelSkypeMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.SkypeSerializer


class ModelGitAccountMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.GitAccountSerializer
