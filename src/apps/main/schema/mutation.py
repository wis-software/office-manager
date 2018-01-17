from django.utils.translation import ugettext_lazy as _
from graphene import Field, Argument, String
from graphene.utils.get_unbound_function import get_unbound_function
from graphene_django.rest_framework.serializer_converter import \
    convert_serializer_to_input_type
from graphene_django.rest_framework.types import ErrorType
from graphene_django_extras import DjangoSerializerMutation


class BaseMutationSerializer(DjangoSerializerMutation):

    non_field_error = String()

    @classmethod
    def get_mutation_field(cls, method_name):
        metadata = cls.Mutation.mapper.get(method_name)
        input_type = metadata.get('input_type',
                                  convert_serializer_to_input_type(
                                      metadata.get('serializer')
                                  ))
        input_field = metadata.get('input_field', 'data')
        permissions = metadata.get('permissions', ())
        argument = {input_field: Argument(input_type)}
        resolver = get_unbound_function(getattr(cls, method_name))
        resolver = cls.wrap_permissions(resolver, permissions)
        result_type = metadata.get('output_type', cls._meta.output)
        return Field(result_type, args=argument, resolver=resolver)

    @classmethod
    def wrap_permissions(cls, func, permissions):
        def wrapper(root, info, **kwargs):
            if permissions:
                for perm_cls in permissions:
                    if not perm_cls().has_permission(info.context, None):
                        return cls(ok=False, errors=None,
                                   non_field_error=_('Permission denied'))
            return func(root, info, **kwargs)

        return wrapper

    @classmethod
    def get_serializer_errors(cls, serializer):
        errors = [
            ErrorType(field=field, messages=e)
            for field, e in serializer.errors.items()
        ]
        return cls(ok=False, errors=list(errors))

    @classmethod
    def get_formatted_data(cls, method_name, data):
        metadata = cls.Mutation.mapper.get(method_name)
        field = metadata.get('input_field', 'data')
        if field:
            data = data.get(field)
        return data

    class Meta:
        abstract = True
