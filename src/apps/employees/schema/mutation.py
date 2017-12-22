from graphene_django_extras import DjangoSerializerMutation
from rest_framework import serializers

from apps.employees import models


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = '__all__'


class ModelEmployeeMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = EmployeeSerializer


class ModelPositionMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = PositionSerializer


class ModelSpecializationMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = SpecializationSerializer
