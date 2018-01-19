from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Tag'
]


class Tag(models.Model):

    name = models.CharField(_('name'), max_length=256, unique=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
