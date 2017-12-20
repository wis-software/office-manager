import graphene

from graphene_django.types import ObjectType
from graphene_django_extras import (
    DjangoFilterPaginateListField, LimitOffsetGraphqlPagination
)

from apps.employees import models
from apps.employees.schema import mutation
from apps.employees.schema import types


class Query(ObjectType):
    positions = DjangoFilterPaginateListField(
        types.PositionType,
        pagination=LimitOffsetGraphqlPagination()
    )

    specializations = DjangoFilterPaginateListField(
        types.SpecializationType,
        pagination=LimitOffsetGraphqlPagination()
    )

    employees = DjangoFilterPaginateListField(
        types.EmployeeType,
        pagination=LimitOffsetGraphqlPagination()
    )

    def resolve_specializations(self, info):
        return models.Specialization.objects.all()

    def resolve_positions(self, info):
        return models.Position.objects.all()


class Mutation(ObjectType):
    position_create = mutation.PositionMutation.CreateField()
    position_update = mutation.PositionMutation.UpdateField()
    position_delete = mutation.PositionMutation.DeleteField()

    specialization_create = mutation.SpecializationMutation.CreateField()
    specialization_update = mutation.SpecializationMutation.UpdateField()
    specialization_delete = mutation.SpecializationMutation.DeleteField()

    employee_create = mutation.EmployeeMutation.CreateField()
    employee_update = mutation.EmployeeMutation.UpdateField()
    employee_delete = mutation.EmployeeMutation.DeleteField()


schema = graphene.Schema(query=Query, mutation=Mutation)
