from django.contrib.auth import login
from graphene_django_extras import DjangoSerializerMutation
from rest_framework import permissions

from apps.employees.schema import serializers as app_serializers
from apps.main.schema.mutation import BaseMutationSerializer
from apps.main.schema.types import ResultResponse
from office import settings


class ModelEmployeeMutation(BaseMutationSerializer):

    @classmethod
    def password_mutation(cls, root, info, **kwargs):
        """
        Change employee password.
        Change password for current employee if we have no passed employee value.

        :param root:
        :param info:
        :param kwargs:
        :return:
        """
        user = info.context.user
        data = cls.get_formatted_data('password_mutation', kwargs)
        serializer = app_serializers.ChangePasswordSerializer(data=data,
                                                              user=user)
        if not serializer.is_valid():
            return cls.get_serializer_errors(serializer)
        user = serializer.user
        new_password = serializer.validated_data['password']
        user.set_password(new_password)
        user.save()
        if settings.DEBUG and user == info.context.user:
            login(user=user, request=info.context)
        return cls(ok=True, errors=None)

    @classmethod
    def create_mutation(cls, root, info, **kwargs):
        data = cls.get_formatted_data('create_mutation', kwargs)
        serializer = app_serializers.EmployeeCreateSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return cls.perform_mutate(obj, info)
        return cls.get_serializer_errors(serializer)

    @classmethod
    def current_employee_mutation(cls, root, info, **kwargs):
        data = cls.get_formatted_data('current_employee_mutation', kwargs)
        employee = info.context.user.employee
        serializer = app_serializers.EmployeeUpdateSerializer(
            instance=employee, data=data
        )
        if not serializer.is_valid():
            return cls.get_serializer_errors(serializer)
        obj = serializer.save()
        return cls.perform_mutate(obj, info)

    class Mutation:
        mapper = {
            'password_mutation': {
                'serializer': app_serializers.ChangePasswordSerializer,
                'output_type': ResultResponse,
            },
            'create_mutation': {
                'serializer': app_serializers.EmployeeCreateSerializer,
            },
            'current_employee_mutation': {
                'serializer': app_serializers.EmployeeUpdateSerializer,
            }
        }

    class Meta:
        serializer_class = app_serializers.EmployeeSerializer
        input_field_name = 'employee'


class ModelPositionMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.PositionSerializer
        input_field_name = 'position'


class ModelSpecializationMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.SpecializationSerializer
        input_field_name = 'specialization'
