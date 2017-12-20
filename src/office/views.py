from graphene_django.views import GraphQLView
from rest_framework.decorators import (
    permission_classes, api_view
)
from rest_framework.permissions import IsAuthenticated


class DRFAuthenticatedGraphQLView(GraphQLView):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        # view = api_view(['GET', 'POST'])(view)
        return view
