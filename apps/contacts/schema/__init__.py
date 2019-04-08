from graphene_django.types import ObjectType
from graphene_django_extras import DjangoFilterPaginateListField

from apps.contacts.schema import mutation
from apps.contacts.schema import types

__all__ = [
    'ContactsQuery', 'ContactsMutation'
]


class ContactsQuery(ObjectType):
    email_contacts = DjangoFilterPaginateListField(types.EmailType)
    phone_contacts = DjangoFilterPaginateListField(types.PhoneNumberType)
    skype_contacts = DjangoFilterPaginateListField(types.SkypeType)
    git_contacts = DjangoFilterPaginateListField(types.GitAccountType)

    class Meta:
        abstract = True


class ContactsMutation(ObjectType):
    email_contact_create = mutation.ModelEmailMutation.CreateField()
    email_contact_update = mutation.ModelEmailMutation.UpdateField()
    email_contact_delete = mutation.ModelEmailMutation.DeleteField()

    phone_contact_create = mutation.ModelPhoneNumberMutation.CreateField()
    phone_contact_update = mutation.ModelPhoneNumberMutation.UpdateField()
    phone_contact_delete = mutation.ModelPhoneNumberMutation.DeleteField()

    skype_contact_create = mutation.ModelSkypeMutation.CreateField()
    skype_contact_update = mutation.ModelSkypeMutation.UpdateField()
    skype_contact_delete = mutation.ModelSkypeMutation.DeleteField()

    git_contact_create = mutation.ModelGitAccountMutation.CreateField()
    git_contact_update = mutation.ModelGitAccountMutation.UpdateField()
    git_contact_delete = mutation.ModelGitAccountMutation.DeleteField()

    class Meta:
        abstract = True
