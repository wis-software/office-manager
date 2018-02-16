from graphene_django.types import ObjectType
from graphene_django_extras import DjangoFilterPaginateListField

from apps.employees.schema import mutation
from apps.employees.schema import types

__all__ = [
    'EmployeeQuery', 'EmployeeMutation'
]


class EmployeeQuery(ObjectType):
    positions = DjangoFilterPaginateListField(types.PositionType)
    specializations = DjangoFilterPaginateListField(types.SpecializationType)
    employees = DjangoFilterPaginateListField(types.EmployeeType)

    class Meta:
        abstract = True


class EmployeeMutation(ObjectType):
    position_create = mutation.ModelPositionMutation.CreateField()
    position_update = mutation.ModelPositionMutation.UpdateField()
    position_delete = mutation.ModelPositionMutation.DeleteField()

    specialization_create = mutation.ModelSpecializationMutation.CreateField()
    specialization_update = mutation.ModelSpecializationMutation.UpdateField()
    specialization_delete = mutation.ModelSpecializationMutation.DeleteField()

    employee_create = mutation.ModelEmployeeMutation.get_mutation_field(
        'create_mutation'
    )
    employee_update = mutation.ModelEmployeeMutation.get_mutation_field(
        'update_mutation'
    )
    employee_delete = mutation.ModelEmployeeMutation.get_mutation_field(
        'delete_mutation'
    )

    change_password = mutation.ModelEmployeeMutation.get_mutation_field(
        'password_mutation'
    )

    change_current_employee = mutation.ModelEmployeeMutation.get_mutation_field(
        'current_employee_mutation'
    )

    class Meta:
        abstract = True
