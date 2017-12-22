
from graphene_django.types import DjangoObjectType


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


class PositionType(DjangoObjectType):
    """
    Position graphQL type.
    Implemented total_employees and employees objects.
    """

    class Meta:
        model = models.Position
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact']
        }


class SpecializationType(DjangoObjectType):
    class Meta:
        model = models.Specialization
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact'],
        }
