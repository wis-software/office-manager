import graphene

from apps.employees import schema as employee_schema
from apps.library import schema as library_schema


class Query(employee_schema.EmployeeQuery, library_schema.LibraryQuery):
    pass


class Mutation(employee_schema.EmployeeMutation, library_schema.LibraryMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
