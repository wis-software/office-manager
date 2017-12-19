import graphene

from graphene_django.types import DjangoObjectType, ObjectType
from graphene_django_extras import (
    DjangoFilterPaginateListField, LimitOffsetGraphqlPagination
)

from apps.employees import models


class EmployeeType(DjangoObjectType):
    class Meta:
        model = models.Employee

        filter_fields = {
            'first_name': ['icontains', 'istartswith'],
            'last_name': ['icontains', 'istartswith'],
            'position': ['exact'],
            'id': ['exact']
        }
        interfaces = (graphene.relay.Node,)


class PositionType(DjangoObjectType):
    """
    Position graphQL type.
    Implemented total_employees and employees objects.
    """
    employees = DjangoFilterPaginateListField(
        EmployeeType,
        pagination=LimitOffsetGraphqlPagination()
    )
    total_employees = graphene.Int()

    def resolve_total_employees(self, info):
        return self.employees.count()

    def resolve_employees(self, info):
        return self.employees.all()

    class Meta:
        model = models.Position
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact']
        }
        interfaces = (graphene.relay.Node,)


class SpecializationType(DjangoObjectType):
    class Meta:
        model = models.Specialization
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact'],
        }
        interfaces = (graphene.relay.Node,)


class Query(ObjectType):
    positions = DjangoFilterPaginateListField(
        PositionType,
        pagination=LimitOffsetGraphqlPagination()
    )

    specializations = DjangoFilterPaginateListField(
        SpecializationType,
        pagination=LimitOffsetGraphqlPagination()
    )

    employees = DjangoFilterPaginateListField(
        EmployeeType,
        pagination=LimitOffsetGraphqlPagination()
    )

    def resolve_specializations(self, info):
        return models.Specialization.objects.all()

    def resolve_positions(self, info):
        return models.Position.objects.all()


schema = graphene.Schema(query=Query)
