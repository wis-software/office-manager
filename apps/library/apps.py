from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BooksConfig(AppConfig):
    name = 'apps.library'
    verbose_name = _('library')
