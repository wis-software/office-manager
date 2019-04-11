import graphene

from apps.employees import schema as employee_schema
from apps.contacts import schema as contacts_schema
from apps.library import schema as library_schema


class Query(employee_schema.EmployeeQuery,
            library_schema.LibraryQuery,
            contacts_schema.ContactsQuery):
    pass


class Mutation(employee_schema.EmployeeMutation,
               library_schema.LibraryMutation,
               contacts_schema.ContactsMutation):
    pass

# pylint: disable=C0103
schema = graphene.Schema(query=Query, mutation=Mutation)
