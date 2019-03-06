from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from office.views import DRFAuthenticatedGraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^graphql/$', DRFAuthenticatedGraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

