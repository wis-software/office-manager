from graphene_django_extras import DjangoSerializerMutation

from apps.employees.schema import serializers as app_serializers


class ModelEmployeeMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.EmployeeSerializer


class ModelPositionMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.PositionSerializer


class ModelSpecializationMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.SpecializationSerializer
