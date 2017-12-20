from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    'Position'
]


class Position(models.Model):

    name = models.CharField(_('name'), max_length=512, default='', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('position')
        verbose_name_plural = _('positions')

