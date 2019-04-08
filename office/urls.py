from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url

from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)

from office.views import DRFAuthenticatedGraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/$', obtain_jwt_token),
    url(r'^api-token-refresh/$', refresh_jwt_token),
    url(r'^api-token-verify/$', verify_jwt_token),
    url(r'^graphql/$', DRFAuthenticatedGraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

