from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from graphene_django.views import GraphQLView
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


def check_jwt_decorator(func):
    """
    Check JWT Token by using DRF Authentication class.
    Returns UNAUTHORIZED response if headers don't contain alive token.

    :param func:
    :return:
    """

    def wrap(request, *args, **kwargs):
        if settings.DEBUG:
            if request.user.is_authenticated():
                return func(request, *args, **kwargs)
        try:
            auth_tuple = JSONWebTokenAuthentication().authenticate(request)
        except APIException as e:
            return JsonResponse({'details': str(e)}, status=e.status_code)
        except Exception as e:
            raise e
        if auth_tuple is None:
            return JsonResponse({'details': _('Unauthorized user')},
                                status=status.HTTP_401_UNAUTHORIZED)
        request.user, request.auth = auth_tuple
        return func(request, *args, **kwargs)

    return wrap


class DRFAuthenticatedGraphQLView(GraphQLView):
    """
    Extended default GraphQLView.
    """

    @method_decorator(check_jwt_decorator)
    def dispatch(self, request, *args, **kwargs):
        return super(DRFAuthenticatedGraphQLView, self).dispatch(
            request, *args, **kwargs)
