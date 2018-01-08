import graphene

from apps.employees import schema as employee_schema
from apps.contacts import schema as contacts_schema


class Query(employee_schema.EmployeeQuery, contacts_schema.ContactsQuery):
    pass


class Mutation(employee_schema.EmployeeMutation,
               contacts_schema.ContactsMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
