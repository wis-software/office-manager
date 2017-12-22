import graphene

from apps.employees import schema as employee_schema


class Query(employee_schema.EmployeeQuery):
    pass


class Mutation(employee_schema.EmployeeMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
