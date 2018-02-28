from django.contrib.auth import login
from django.conf import settings
from graphene_django_extras import DjangoSerializerMutation

from apps.employees.schema import serializers as app_serializers
from apps.employees.models import Employee
from apps.employees.schema.types import IDType
from apps.main.schema.mutation import SerializerMutation
from apps.main.schema.types import ResultResponse


class ModelEmployeeMutation(SerializerMutation):

    @classmethod
    def password_mutation(cls, root, info, serializer_class, input_field_name,
                          **kwargs):
        """
        Change employee password.
        Change password for current employee if we have no passed employee value.
        """
        data = cls.get_formatted_data(input_field_name, kwargs)
        user = info.context.user
        serializer = serializer_class(data=data, user=user)
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
    def current_employee_mutation(cls, root, info, serializer_class,
                                  input_field_name, **kwargs):
        """
        Change employee data for current user.
        """
        data = cls.get_formatted_data(input_field_name, kwargs)
        employee = info.context.user.employee
        serializer = serializer_class(instance=employee, data=data)
        if not serializer.is_valid():
            return cls.get_serializer_errors(serializer)
        obj = serializer.save()
        return cls._perform_mutate(obj, info)

    class Meta:
        input_field_name = 'employee'
        model = Employee
        rules = {
            'password_mutation': {
                'serializer': app_serializers.ChangePasswordSerializer,
                'output_type': ResultResponse,
            },
            'delete_mutation': {
                'input_type': IDType
            },
            'create_mutation': {
                'serializer': app_serializers.EmployeeCreateSerializer,
            },
            'update_mutation': {
                'serializer': app_serializers.EmployeeUpdateSerializer
            },
            'current_employee_mutation': {
                'serializer': app_serializers.CurrentEmployeeUpdateSerializer
            }
        }


class ModelPositionMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.PositionSerializer
        input_field_name = 'position'


class ModelSpecializationMutation(DjangoSerializerMutation):
    class Meta:
        serializer_class = app_serializers.SpecializationSerializer
        input_field_name = 'specialization'
