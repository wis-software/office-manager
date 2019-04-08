from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from office.views import DRFAuthenticatedGraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api-token-refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api-token-verify/$', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^graphql/$', DRFAuthenticatedGraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

