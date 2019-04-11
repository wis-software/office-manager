from collections import OrderedDict

import graphene
from graphene.types.base import BaseOptions
from graphene.utils.get_unbound_function import get_unbound_function
from django.utils.translation import ugettext_lazy as _
from graphene_django.rest_framework.serializer_converter import \
    convert_serializer_to_input_type
from graphene_django.rest_framework.types import ErrorType
from graphene_django import DjangoObjectType
from graphene_django_extras.base_types import object_type_factory
from graphene_django_extras.utils import get_Object_or_None


class SerializerMutationOptions(BaseOptions):
    fields = None
    input_fields = None
    interfaces = ()
    serializer_class = None
    rules = None
    action = None
    arguments = None
    output = None
    resolver = None


class SerializerMutation(graphene.ObjectType):
    non_field_error = graphene.String(description='Non field error message')
    ok = graphene.Boolean(
        description='Boolean field that return mutation result request.')
    errors = graphene.List(ErrorType, description='Errors list for the field')

    # pylint: disable=W0613,W0221
    @classmethod
    def __init_subclass_with_meta__(cls, rules=None, input_field_name='data',
                                    model=None, output_field_name='data',
                                    serializer_class=None,
                                    description='', **options):
        if not rules:
            raise Exception('rules not defined')

        description = description or 'SerializerMutation for {} model'.format(
            model.__name__)

        # pylint: disable=W0201
        _meta = SerializerMutationOptions(cls)
        outputType = object_type_factory(DjangoObjectType, new_model=model)
        _meta.output_type = outputType
        _meta.fields = OrderedDict({
            'instance': graphene.Field(outputType)
        })
        _meta.rules = rules
        _meta.output = cls
        _meta.serializer_class = serializer_class
        _meta.model = model
        _meta.input_field_name = output_field_name

        super(SerializerMutation, cls).__init_subclass_with_meta__(
            _meta=_meta, description=description, **options
        )

    @classmethod
    def _get_serializer_class(cls, method_name):
        """
        Return serializer class from Meta rules attribute.
        Would be used for overriding.

        :param method_name: str Mutation method name
        :return: serializers
        """
        return cls._meta.rules[method_name].get(
            'serializer', cls._meta.serializer_class
        )

    @classmethod
    def _get_permission_classes(cls, method_name):
        """
        Return permission classes.
        Would be used for overriding.

        :param method_name: str Mutation method name
        :return:
        """
        return cls._meta.rules[method_name].get('permission_classes', ())

    @classmethod
    def _get_input_type(cls, method_name):
        """
        Return input type for validation data from request.

        :param method_name: str Mutation method name
        :return: graphene.InputObjectType subclass object
        """
        input_type = cls._meta.rules[method_name].get('input_type', None)
        if not input_type:
            serializer_class = cls._get_serializer_class(method_name)
            if serializer_class:
                input_type = convert_serializer_to_input_type(serializer_class)
        assert input_type, _("Input type is required")
        return input_type

    @classmethod
    def _get_output_type(cls, method_name):
        """
        Return output type for mutation response.

        :param method_name: str Mutation method name
        :return:
        """
        return cls._meta.rules[method_name].get('output_type', cls)

    @classmethod
    def get_mutation_field(cls, method_name, serializer_class=None):
        """
        Return mutation field with all attached metadata.

        :param method_name: str Mutation method name
        :return: function Resolver
        """
        assert method_name in cls._meta.rules, \
            'Rule for \"%s\" does not exist' % method_name

        serializer_class = serializer_class or \
                           cls._get_serializer_class(method_name)
        permissions = cls._get_permission_classes(method_name)
        input_field = cls._meta.input_field_name
        input_type = cls._get_input_type(method_name)
        output_type = cls._get_output_type(method_name)
        argument = {input_field: graphene.Argument(input_type)}
        resolver = get_unbound_function(getattr(cls, method_name))
        resolver = cls._wrap_extra_data(resolver, permissions=permissions,
                                        serializer_class=serializer_class,
                                        input_field_name=input_field)
        return graphene.Field(output_type, args=argument, resolver=resolver)

    @classmethod
    def _wrap_extra_data(cls, func, permissions, serializer_class,
                         input_field_name):
        """
        Wrapper for mutation method, which use metadata from Meta class.

        :param func: function Mutation method
        :param permissions: tuple Permission classes
        :param serializer_class: serializers.Serializer class or subclass
        :param input_field_name: str Input field name
        :return: function Wrapped function
        """

        def wrapper(root, info, **kwargs):
            # check permissions for mutation endpoint
            for perm_cls in permissions:
                if not perm_cls().has_permission(info.context, None):
                    return cls(ok=False, errors=None,
                               non_field_error=_('Permission denied'))
            return func(root, info, serializer_class=serializer_class,
                        input_field_name=input_field_name, **kwargs)

        return wrapper

    @classmethod
    def get_serializer_errors(cls, serializer):
        """
        Return error response with all serializer's errors

        :param serializer: object serializer instance
        :return: cls
        """
        errors = [
            ErrorType(field=field, messages=e)
            for field, e in serializer.errors.items()
        ]
        return cls(ok=False, errors=list(errors))

    @classmethod
    def get_formatted_data(cls, input_field_name, data):
        """
        Request data converter, would be used before passing data into serializer.

        :param method_name: str Mutation method name
        :param input_field_name: str Key in data
        :param data: dict
        :return: dict
        """
        return data.get(input_field_name, None)

    # pylint: disable=E1121
    # probable reasons:
    # https://github.com/PyCQA/pylint/issues/2172
    # https://github.com/PyCQA/pylint/issues/1789
    @classmethod
    def create_mutation(cls, root, info, serializer_class, input_field_name,
                        **kwargs):
        """ Base CREATE mutation. """
        data = cls.get_formatted_data(input_field_name, kwargs)
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return cls._perform_mutate(obj, info)
        return cls.get_serializer_errors(serializer)

    @classmethod
    def delete_mutation(cls, root, info, serializer_class, input_field_name,
                        **kwargs):
        """ Base CREATE mutation. """
        data = cls.get_formatted_data(input_field_name, kwargs)
        object_id = data['id']
        obj = get_Object_or_None(cls._meta.model, pk=object_id)
        if obj:
            obj.delete()
            return cls(ok=True, errors=None, instance=None)
        return cls(ok=False, non_field_error=_('Object does not exist'))

    @classmethod
    def update_mutation(cls, root, info, serializer_class, input_field_name,
                        **kwargs):
        """ Base UPDATE mutation. """
        data = cls.get_formatted_data(input_field_name, kwargs)
        object_id = data['id']
        old_obj = get_Object_or_None(cls._meta.model, pk=object_id)
        if old_obj:
            obj_data = serializer_class(instance=old_obj).data
            obj_data.update(data)
            serializer = serializer_class(instance=old_obj, data=obj_data)
            if serializer.is_valid():
                obj = serializer.save()
                return cls._perform_mutate(obj, info)
            return cls.get_serializer_errors(serializer)
        return cls(ok=False, non_field_error=_('Object does not exist'))

    @classmethod
    def _perform_mutate(cls, obj):
        data = {'instance': obj, 'ok': True, 'errors': None}
        return cls(**data)

    class Meta:
        abstract = True
