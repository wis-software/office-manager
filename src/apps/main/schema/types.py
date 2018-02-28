import graphene
from graphene_django.rest_framework.types import ErrorType


class ResultResponse(graphene.ObjectType):
    ok = graphene.Boolean(
        description='Boolean field that return mutation result request.'
    )
    errors = graphene.List(ErrorType, description='Errors list for the field')
